/*
 * Plugin for WYMEditor that provides an interface to allow separation
 * of presentation and content by allowing the user to select presentation
 * elements for each section.  Depends on a server-side backend to do
 * parsing and provide list of allowed CSS classes.
 */

function PresentationControls(wym, opts) {
    this.wym = wym;
    this.opts = opts;
    this.name = wym._element.get(0).name;
    // availableStyles: an array of dictionaries corresponding to PresentationInfo objects
    // (PresentationClass objects specifically)
    this.availableStyles = new Array();
    // presentationInfo: a dictionary of { sectId : [PresentationInfo] }
    this.presentationInfo = {};

    // commands: an array of dictionaries corresponding to PresentationInfo objects
    // (PresentationCommand objects specifically)
    this.commands = new Array();
    // commandDict: a dictionary mapping command name to PresentationInfo object.
    this.commandDict = {};

    // a selector which matches any command block.  Filled in later.
    this.allCommandSelectors = "";

    // the node of the current block level element being edited.
    this.currentNode = null;

    // Need to sync with presentation.py
    this.blockdefSelector = "h1,h2,h3,h4,h5,h6,p,ol,ul,blockquote,li,pre";

    this.setupControls(jQuery(wym._bvox).find(".wym_area_bottom"));
}

// ---- Setup and loading ----

// -- Setup static controls

PresentationControls.prototype.setupControls = function(container) {
    var idPrefix = "id_prescontrol_" + this.name + "_";
    var previewButtonId = idPrefix + 'previewbutton';
    var showStylesButtonId = idPrefix + 'showstyles';
    var previewBoxId = idPrefix + 'previewbox';
    var hidePreviewButtonId = idPrefix + 'hidepreviewbutton';
    var cleanHtmlButtonId = idPrefix + 'cleanhtmlbutton';
    var self = this;

    // Create elements
    container.after(
        "<div class=\"prescontrol\">" +
            "<input type=\"submit\" value=\"Clean pasted HTML\" id=\"" + cleanHtmlButtonId  +  "\" />" +
            "<input type=\"submit\" value=\"Preview\" id=\"" + previewButtonId + "\" />" +
            "<input type=\"submit\" id=\"" + showStylesButtonId + "\" />" +
            "<div class=\"prescontrolerror\" id=\"" + idPrefix + "errorbox" + "\"></div>" +
        "</div>");

    jQuery("body").append("<div style=\"position: absolute; display: none\" class=\"previewbox\" id=\"" +  previewBoxId + "\">" +
                          "<div class=\"closebar\">" +
                          "<input type=\"submit\" value=\"Close\" id=\"" + hidePreviewButtonId + "\">" +
                          "</div>" +
                          "<div class=\"content\"></div>" +
                          "</div>");

    this.classList = jQuery(this.wym._options.classesSelector).find("ul");
    this.commandList = jQuery(this.wym._options.layoutCommandsSelector).find("ul");
    this.errorBox = jQuery('#' + idPrefix + "errorbox");
    this.previewButton = jQuery('#' + previewButtonId);
    this.previewBox = jQuery('#' + previewBoxId);
    this.hidePreviewButton = jQuery('#' + hidePreviewButtonId);
    this.showStylesButton = jQuery('#' + showStylesButtonId);
    this.cleanHtmlButton = jQuery('#' + cleanHtmlButtonId);

    this.setupCssStorage();

     // Initial set up

    // retrieveCommands() must come before retrieveStyles(), due to use
    // of calculateSelectors() which needs .commands to be set.
    this.retrieveCommands(); // async=False
    this.retrieveStyles(); // async=False
    this.separatePresentation();

    this.previewButton.click(function(event) {
                                 self.showPreview();
                                 return false;
                              });
    this.hidePreviewButton.click(function(event) {
                                     self.previewBox.hide();
                                     return false;
                                 });
    // start with styles hidden
    this.showStyles(false);
    this.showStylesButton.toggle(function(event) {
                                     self.showStyles(true);
                                     return false;
                                 },
                                 function(event) {
                                     self.showStyles(false);
                                     return false;
                                 });
    this.cleanHtmlButton.click(function(event) {
                                   self.cleanHtml();
                                   return false;
                               });
    jQuery(this.wym._doc)
        .bind("keyup", function(evt) {
                  // this style of binding gives docKeyup
                  // access to 'this' PresentationControl
                  self.docKeyup(evt);
              })
        .bind("keydown", function(evt) {
                  self.docKeydown(evt);
              })
        .bind("mouseup", function(evt) {
                  // In case the user clicked somewhere else
                  // in the document, we have to update class list
                  self.updateAppliedButtons();
              });
    jQuery(this.wym._options.containersSelector).find("a")
        .bind("mousedown", function(evt) {
                  // Need to save element id before the 'click' event
                  // handler for the button runs and changes the id.
                  self.saveCurrentElemId();
              })
        .bind("click", function(evt) {
                  // Need to restore the element id before anything else
                  // runs and calls ensureId
                  self.restoreCurrentElemId();
                  self.updateAppliedButtons();
              });

    // Insert rewriting of HTML before the WYMeditor updates the textarea.
    jQuery(this.wym._options.updateSelector)
        .bind(this.wym._options.updateEvent, function(event) {
                  self.formSubmit(event);
              });
};

// Setup document - splits the HTML into 'content HTML' and 'presentation'
PresentationControls.prototype.separatePresentation = function() {
    var self = this;
    jQuery.post(this.opts.separatePresentationUrl, { html: self.wym.xhtml() } ,
                function(data) {
                    self.withGoodData(data,
                        function(value) {
                            // Store the presentation
                            self.presentationInfo = value.presentation;
                            // Update the HTML
                            self.setHtml(value.html);
                            // Update presentation of HTML
                            self.updateAfterLoading();
                        });
                }, "json");
};

PresentationControls.prototype.updateAfterLoading = function() {
    this.insertCommandBlocks();
    this.updateAllStyleDisplay();
};

PresentationControls.prototype.retrieveCommands = function() {
    var self = this;
    // Needs async=false, since separatePresentation depends on data.
    var res = jQuery.ajax({
                  type: "GET",
                  data: {},
                  url: this.opts.retrieveCommandsUrl,
                  dataType: "json",
                  async: false
    }).responseText;
    var data = JSON.parse(res);

    self.withGoodData(data, function(value) {
                            self.commands = data.value;
                            for (var i = 0; i < self.commands.length; i++) {
                                var c = self.commands[i];
                                self.commandDict[c.name] = c;
                            }
                            self.calculateSelectors(self.commands);
                            self.allCommandSelectors = jQuery.map(self.commands,
                                                                    function(c, i) { return self.tagnameToSelector(c.name); }
                                                                    ).join(",");
                            self.buildCommandList();
                            jQuery.each(self.commands,
                                function(i, c) {
                                    self.addCssRule(self.tagnameToSelector(c.name) + ":after",
                                                    'content: "' + c.verbose_name + '"');
                                });
                        });
};

PresentationControls.prototype.retrieveStyles = function() {
    var self = this;
    // Needs async=false, since separatePresentation depends on data.
    var res = jQuery.ajax({
                  type: "GET",
                  data: {
                      'template':this.opts.template,
                      'page_id':this.opts.pageId
                  },
                  url: this.opts.retrieveStylesUrl,
                  dataType: "json",
                  async: false
    }).responseText;
    var data = JSON.parse(res);

    self.withGoodData(data, function(value) {
        self.availableStyles = data.value;
        self.calculateSelectors(self.availableStyles);
        self.buildClassList();
    });
};

PresentationControls.prototype.calculateSelectors = function(stylelist) {
    // Given a list of styles, add a 'allowed_elements_selector' attribute
    // on the basis of the 'allowed_elements' attribute.

    // This is just an optimisation to avoid doing this work multiple times.

    var self = this;
    for (var i = 0; i < stylelist.length; i++) {
        var style = stylelist[i];
        style.allowed_elements_selector =
            jQuery.map(style.allowed_elements,
                       function(t,j) { return self.tagnameToSelector(t); }
                      ).join(",");
    }
};

PresentationControls.prototype.tagnameToSelector = function(name) {
    // Convert a tag name into a selector used to match elements that represent
    // that tag.
    //
    // A 'tag' is either an HTML element name or a command name.
    //
    // This function accounts for the use of p elements to represent
    // commands in the document.
    var c = this.commandDict[name];
    if (c == null) {
        // not a command
        if (name == "p") {
            // Need to ensure we don't match commands
            var selector = "p";
            for (var i = 0; i < this.commands.length; i++) {
                selector = selector + "[class!='secommand secommand-" + this.commands[i].name + "']";
            }
            return selector;
        } else {
            return name;
        }
    } else {
        return "p.secommand-" + name;
    }
};

PresentationControls.prototype.setupCssStorage = function() {
    // We need a place to store custom CSS rules. (Existing jQuery plugins don't
    // allow for our need of changing style sheet of document in an iframe, and
    // rolling our own is easier than fixing them).

    // code partly copied from jquery.cssRule.js
    var cssStorageNode = jQuery('<style rel="stylesheet" type="text/css">').appendTo(jQuery(this.wym._doc).find("head"))[0];
    this.stylesheet = this.wym._doc.styleSheets[0];
};

// ---- Saving data ----


PresentationControls.prototype.prepareData = function() {
    // Prepare data/html for sending server side.

    // We need to ensure all elements have ids, *and* that command block
    // elements have correct ids (which is a side effect of the below).
    this.ensureAllIds();
    // this.presentationInfo might have old info, if command blocks have
    // been removed.  Need to clean.
    this.cleanPresentationInfo();
};

PresentationControls.prototype.cleanHtml = function() {
    this.prepareData();
    var self = this;
    var html = this.wym.xhtml();
    jQuery.post(this.opts.cleanHtmlUrl, {'html':html},
                function(data) {
                    self.withGoodData(data, function(value) {
                                            self.setHtml(value.html);
                                            self.updateAfterLoading();
                                        });
                }, "json");
};

// ---- Utility functions ----

PresentationControls.prototype.escapeHtml = function(html) {
    return html.replace(/&/g,"&amp;")
        .replace(/\"/g,"&quot;")
        .replace(/</g,"&lt;")
        .replace(/>/g,"&gt;");
};

PresentationControls.prototype.flattenPresStyle = function(pres) {
    // Convert a PresentationInfo object to a string
    return pres.prestype + ":" + pres.name;
};

// If data contains an error message, display to the user,
// otherwise clear the displayed error and perform the callback
// with the value in the data.
PresentationControls.prototype.withGoodData = function(data, callback) {
    if (data.result == 'ok') {
        this.clearError();
        callback(data.value);
    } else {
        // TODO - perhaps distinguish between a server error
        // and a user error
        this.showError(data.message);
    }
};

// ---- DOM utility ----

PresentationControls.prototype.nextElementSibling = function(node) {
    var next = node;
    while (true) {
        if (next == null) {
            return null;
        }
        if (next.nextSibling == null) {
            next = next.parentNode;
        } else {
            next = next.nextSibling;
            if (next.nodeName != "#text") {
                return next;
            }
        }
    }
};

PresentationControls.prototype.previousElementSibling = function(node) {
    var prev = node;
    while (true) {
        if (prev == null) {
            return null;
        }
        if (prev.previousSibling == null) {
            prev = prev.parentNode;
        } else {
            prev = prev.previousSibling;
            if (prev.nodeName != "#text") {
                return prev;
            }
        }
    }
};

// ---- CSS utility ----

PresentationControls.prototype.addCssRule = function(selector, rule) {
    var ss = this.stylesheet;
    var rules = ss.rules ? 'rules' : 'cssRules';
    // should work with IE and Firefox, don't know about Safari
    if (ss.addRule)
        ss.addRule(selector, rule||'x:y' );//IE won't allow empty rules
    else if (ss.insertRule)
        ss.insertRule(selector + '{'+ rule +'}', ss[rules].length);
};

// ---- Event handlers ----

// Long event handlers below, most are defined inline.

PresentationControls.prototype.docKeyup = function(evt) {
    // Some browsers (Firefox at least) will insert a new paragraph with the
    // same ID as the old one when the user presses 'Enter'. This needs fixing
    // for our styling to work. It's possible that multiple 'p' elements can be inserted
    // for one keyup event, so we handle that. This appears to happen for any
    // elements that are created by pressing 'Enter'

    var node = this.getCurrentContainerNode();
    var container;
    if (node == null) {
        return;
    } else {
        container = jQuery(node);
    }
    if (evt.keyCode == 13 && !evt.shiftKey) {
        if (container.is("p[id],li[id]")) {
            // Need to clear id on all elem's with that id except the first.
            // (hoping that jQuery will return them in document order, which it
            // seems to)
            jQuery(this.wym._doc).find(container.get(0).tagName + "#" +  container.attr("id")).
                each(function(i){
                         var node = this;
                         if (i > 0) { // skip the first
                              jQuery(node).removeAttr('id');
                         }
                     });
        }
    }
    // We also need to update the disable/enabled state of the classList and commandList
    this.updateAppliedButtons(container);
};

PresentationControls.prototype.docKeydown = function(evt) {
    // Need to intercept backspace and delete, to stop command blocks
    // being deleted. (The system copes fairly well with them being
    // deleted, but it can be very confusing for the user.)
    var isBackspace = (evt.keyCode == 8);
    var isDelete = (evt.keyCode == 46);
    var target = null;

    if (isBackspace || isDelete) {

        var s = this.wym._iframe.contentWindow.getSelection();
        if (s.anchorNode != s.focusNode) {
            // an extended selection.  It doesn't matter if this
            // contains command blocks - it doesn't confuse the user
            // if these are deleted wholesale.
            return;
        }
        if (s.focusNode == null) {
            return;
        }

        var node = s.focusNode;
        if (node.nodeName == "#text") {
            // always true?
            node = node.parentNode;
        }
        if (isBackspace) {
            if (s.focusOffset != 0) {
                return; // not at first character within text node
            }
            // need to check *previous* node
            target = this.previousElementSibling(node);
        }
        if (isDelete) {
            if (s.focusOffset != s.focusNode.textContent.length) {
                return; // not at last character within text node
            }
            // need to check *next* node
            target = this.nextElementSibling(node);
        }
        if (target == null) {
            return;
        }

        if (jQuery(target).is(this.allCommandSelectors)) {
            // stop backspace or delete from working.
            evt.preventDefault();
        }
    }
};

PresentationControls.prototype.formSubmit = function(event) {
    this.prepareData();
    // Since we are in the middle of submitting the page, an asynchronous
    // request will be too late! So we block instead.

    // TODO - exception handling.  If this fails, the default
    // handler will post the form, causing all formatting to be lost.
    var res = jQuery.ajax({
                  type: "POST",
                  data: {
                      html: this.wym.xhtml(),
                      presentation: JSON.stringify(this.presentationInfo)
                  },
                  url: this.opts.combinePresentationUrl,
                  dataType: "json",
                  async: false
    }).responseText;
    var data = JSON.parse(res);
    if (data.result == 'ok') {
        // Replace existing HTML with combined.
        this.setHtml(data.value.html);
        // In case the normal WYMeditor update got called *before* this
        // event handler, we do another update.
        this.wym.update();
    } else {
        event.preventDefault();
        this.showError(data.message);
        alert("Data in " + this.name + " can't be saved - see error message.");
    }
};

PresentationControls.prototype.saveCurrentElemId = function() {

    // When a container tag is clicked, the tag of the current node is changed,
    // and the 'id' attribute is removed. This causes the styling and commands
    // to be lost. So we save the id and restore after the change.  This can
    // result in strange ids e.g. an h2 element with the id='h1_1'.  However,
    // this doesn't matter at all - it only matters that ids are unique
    var nodeId = null;
    var node = this.getCurrentContainerNode();
    if (node != null) {
        nodeId = node.id;
    }
    this._savedNodeId = nodeId;
};

PresentationControls.prototype.restoreCurrentElemId = function() {

    if (this._savedNodeId == null) {
        return;
    }
    var node = this.getCurrentContainerNode();
    if (node != null &&
        (node.id == null || node.id == "")) {
        node.id = this._savedNodeId;
    }
    this._savedNodeId = null;
};

// ---- Manipulation of edited document ----

PresentationControls.prototype.setHtml = function(html) {
    // WUMEditor ought to call .listen() after setting
    // the HTML (to rebind events for images),
    // but it doesn't at the moment, so we work around it by wrapping.
    this.wym.html(html);
    this.wym.listen();
};

PresentationControls.prototype.ensureAllIds = function() {
    // We check all block level elements (or all elements that can have commands
    // applied to them)

    var self = this;
    var elems = [];
    for (var i = 0; i < this.commands.length; i++) {
        elems = jQuery.merge(elems, this.commands[i].allowed_elements);
    }
    elems = jQuery.unique(elems);
    jQuery(this.wym._doc).find(elems.join(",")).each(function(i) {
                                                         self.ensureId(this);
                                                     });
};

PresentationControls.prototype.ensureId = function(node) {
    var id = node.id;

    if (id == undefined || id == "") {
        id = this.nextId(node.tagName.toLowerCase());
        node.id = id;
        this.registerSection(id);
    }
    return id;
};

PresentationControls.prototype.nextId = function(tagName) {
    // All sections that can receive styles need a section ID.
    // For the initial HTML, this is assigned server-side when the
    // HTML is split into 'semantic HTML' and 'presentation info'.
    // For newly added HTML, however, we need to add it ourself

    var i = 1;
    var id = "";
    while (true) {
        id = tagName + "_" + i.toString();
        if (jQuery(this.wym._doc).find('#' + id).is(tagName)) {
            i++;
        } else {
            return id;
        }
    }
};

PresentationControls.prototype.commandBlockId = function(sectId, command) {
    // Returns the ID to use for a command block that appears before
    // section sectId for a given command.  This is also the key used
    // in this.presentationInfo
    return command.name + "_" + sectId;
};

PresentationControls.prototype.insertCommandBlock = function(sectId, command) {
    // the spaces help make the command a decent target in the editor for Firefox (and we also use z-index: 1 in the CSS to bring them forward) - otherwise we can't hit them reliably with the mouse. Safari has not had a problem with this for some reason.
    var newelem = jQuery("<p class=\"secommand secommand-" + command.name + "\">&nbsp;</p>");
    var elem = jQuery(this.wym._doc).find("#" + sectId);

    // Commands have an order they should appear in, which is defined by layout_order.
    // We can use this to put the block in the right place.
    var loopAgain = true;
    var self = this;
    while(loopAgain) {
        loopAgain = false;
        jQuery.each(this.commands,
                   function(i, c) {
                       var prev = elem.prev();
                       if (prev.is(self.tagnameToSelector(c.name)) &&
                                   c.layout_order > command.layout_order) {
                           elem = prev;
                           loopAgain = true;
                       }
                   });
    }

    elem.before(newelem);
    var newId = this.commandBlockId(sectId, command);
    newelem.attr('id', newId);
    return newId;
};

PresentationControls.prototype.insertCommandBlocks = function() {
    // This is run once, after loading HTML.  We can rely on 'ids' being
    // present, since the HTML is all sent by the server.
    for (var key in this.presentationInfo) {
        var presinfos = this.presentationInfo[key];
        for (var i = 0; i < presinfos.length; i++) {
            var pi = presinfos[i];
            if (pi.prestype == 'command') {
                // key = e.g. 'newrow_p_1', we need 'p_1'
                var id = key.split('_').slice(1).join('_');
                this.insertCommandBlock(id, this.commandDict[pi.name]);
            }
        }
    }
};

PresentationControls.prototype.isCommandBlock = function(node) {
    // command blocks are like <p id="newrow_p_1" class="secommand secommand-[commandname]">
    return (node != undefined && node.tagName != undefined &&
            node.tagName.toLowerCase() == 'p' && node.className != undefined &&
            node.className.match(/\bsecommand\b/));
};

// ---- Display of style information on document.

PresentationControls.prototype.updateStyleDisplay = function(sectId) {
    var styles = this.presentationInfo[sectId];
    var self = this;
    var stylelist = jQuery.map(styles, function(s, i) {
                                   return self.getVerboseStyleName(s.name);
                               }).join(", ");
    // put a non-breaking space into the style list, so it always exists                           
    this.addCssRule("#" + sectId + ":before", 'content: "' + stylelist + '\\00a0' + '"');
};

PresentationControls.prototype.updateAllStyleDisplay = function() {
    for (var key in this.presentationInfo) {
        this.updateStyleDisplay(key);
    }
};

PresentationControls.prototype.getVerboseStyleName = function(stylename) {
    // Full style information is not stored against individual headings, only
    // the type and name. So sometimes we need to go from one to the other.

    var styles = this.availableStyles;
    for (var i = 0; i < styles.length; i++) {
        if (styles[i].name == stylename) {
            return styles[i].verbose_name;
        }
    }
    var commands = this.commands;
    for (var i2 = 0; i2 < commands; i2++) {
        if (commands[i2].name == stylename) {
            return commands[i2].verbose_name;
        }
    }
    return undefined; // shouldn't get here
};

// ---- Manipulation of class and command list ----

PresentationControls.prototype.buildClassList = function() {
    var self = this;
    this.classList.empty();
    // For each new category encountered, we have an li that contains
    // a div with a heading, and a ul with all the actual classes.
    // NB the category could be 'null' so care must be taken. Also,
    // the list is already sorted by category and verbose_name
    var state = {start:true,
                 category:null,
                 categoryList:null
                };
    jQuery.each(self.availableStyles, function(i, item) {
        if (state.start || (state.category != item.category)) {
            var category;
            if (item.category == null) {
                category = "Uncategorized";
            } else {
                category = item.category;
            }
            var classListItem = jQuery("<li class=\"class-category\"><h3 class=\"categoryHeading\">" + self.escapeHtml(category) + ':</h3></li>');
            classListItem.appendTo(self.classList);
            state.categoryList = jQuery("<ul></ul>");
            state.categoryList.appendTo(classListItem);
        }
        var btn = jQuery("<li><a href='#'>" + self.escapeHtml(item.verbose_name) + "</a></li>").appendTo(state.categoryList).find("a");
        // event handlers
        var style = self.availableStyles[i];

        btn.click(function(event) {
                      self.toggleStyle(style, btn);
                      event.preventDefault();
                  });
        state.start = false;
        state.category = item.category;
    });
};

PresentationControls.prototype.buildCommandList = function () {
    var self = this;
    self.commandList.empty();
    jQuery.each(self.commands, function(i, item) {
        var btn = jQuery("<li><a href='#'>" + self.escapeHtml(item.verbose_name) + "</a></li>").appendTo(self.commandList).find("a");
        // event handlers
        var command = self.commands[i];

        btn.click(function(event) {
                      self.doCommand(command, btn);
                      event.preventDefault();
                  });
    });
};

PresentationControls.prototype.updateClassListItem = function(btn, style) {
    var sectId = this.getCurrentSection(style);
    if (sectId == undefined) {
        // Can't use it.
        if (style.prestype == "command") {
            // Don't want the class list (displayed below command list)
            // to jump up and down
            btn.addClass("disabled");
            btn.removeClass("used");
        } else {
            btn.hide();
        }
    } else {
        if (style.prestype == "command") {
            btn.removeClass("disabled");
            if (this.hasCommand(sectId, style)) {
                btn.addClass("used");
            } else {
                btn.removeClass("used");
            }
        } else {
            btn.show();
            if (this.hasStyle(sectId, style)) {
                btn.addClass("used");
            } else {
                btn.removeClass("used");
            }
        }
    }
};

PresentationControls.prototype.updateAppliedButtons = function(curContainer) {
    var self = this;
    var node;
    if (curContainer == undefined) {
        node = this.getCurrentContainerNode();
    } else {
        node = curContainer.get(0);
    }
    if (node != undefined && node != this.currentNode) {
        // if current node has changed, might need to update list
        this.currentNode = node;
        // Sets enabled/disabled on all items in classList and commands
        var pairs = [[this.availableStyles, this.classList],
                     [this.commands, this.commandList]];

        for (var i = 0; i < pairs.length; i++) {
            var styles = pairs[i][0];
            var btncontainer = pairs[i][1];
            btncontainer.find("a").each(function(k) {
                                            self.updateClassListItem(jQuery(this), styles[k]);
                                        });
        }

        // We also update the container list to set the class="used" for
        // consistent styling between that list and the command/class lists.
        jQuery(this.wym._options.containersSelector).find("a").each(function(k) {
            var name = this.name; // stores 'P', 'H1' etc
            if (name.toLowerCase() == node.tagName.toLowerCase() &&
                !self.isCommandBlock(node)) {
                jQuery(this).addClass("used");
            } else {
                jQuery(this).removeClass("used");
            }
        });

    }
};

// ---- Manipulation/query of stored presentation info ----

PresentationControls.prototype.registerSection = function(sectId) {
    // Make sure we have somewhere to store styles for a section.
    this.presentationInfo[sectId] = new Array();
};

PresentationControls.prototype.getCurrentContainerNode = function() {
    // Returns the node of the closest container element to the selection
    var container = jQuery(this.wym.selected()).parentsOrSelf(this.blockdefSelector);
    if (container.is(this.blockdefSelector)) {
        return container.get(0);
    } else {
        return null;
    }
};

PresentationControls.prototype.getCurrentSection = function(style) {
    // Returns the section ID of the current section that is applicable
    // to the given style, or undefined if there is none.
    // Since sections can be nested, if more than one section is possible
    // for the given style, the first section found (starting from the
    // current selection and moving up the HTML tree) will be returned.
    // This function has the side effect of adding a section ID if one
    // was not defined already.
    var wym = this.wym;
    var self = this;
    var expr = style.allowed_elements_selector;
    var container = jQuery(wym.selected()).parentsOrSelf(expr);
    if (container.is(expr)) {
        var first = container.get(0);
        var id = this.ensureId(first);
        return id;
    }
    return undefined;
};

PresentationControls.prototype.hasStyle = function(sectId, style) {
    var styles = this.presentationInfo[sectId];
    if (styles == undefined)
        return false;
    for (var i = 0; i < styles.length; i++) {
        if (this.flattenPresStyle(styles[i]) == this.flattenPresStyle(style)) {
            return true;
        };
    }
    return false;
};

PresentationControls.prototype.hasCommand = function(sectId, command) {
    // Returns true if the section has the command before it.
    return (this.presentationInfo[this.commandBlockId(sectId, command)] != undefined);
};

PresentationControls.prototype.addStyle = function(sectId, presinfo) {
    var styles = this.presentationInfo[sectId];
    styles.push(presinfo);
    this.presentationInfo[sectId] = jQuery.unique(styles);
};

PresentationControls.prototype.removeStyle = function(sectId, presinfo) {
    var styles = this.presentationInfo[sectId];
    styles = jQuery.grep(styles, function(item, i) {
                             return !(item.prestype == presinfo.prestype
                                      && item.name == presinfo.name);
                         });
    this.presentationInfo[sectId] = styles;
};

PresentationControls.prototype.toggleStyle = function(style, btn) {
    // What section are we on?
    var sectId = this.getCurrentSection(style);
    if (sectId == undefined) {
        // No allowed to use it there
        alert("Cannot use this style on current element.");
        return;
    }

    if (this.hasStyle(sectId, style)) {
        this.removeStyle(sectId, style);
    } else {
        this.addStyle(sectId, style);
    }
    this.updateStyleDisplay(sectId);
    this.updateClassListItem(btn, style);
};

PresentationControls.prototype.doCommand = function(command, btn) {
    // What section are we on?
    var sectId = this.getCurrentSection(command);
    if (sectId == undefined) {
        // Not allowed to use it there
        alert("Cannot use this command on current element.");
        return;
    }
    // newrow and newcol are the only commands at the moment.
    // We handle both using inserted blocks, and both commands
    // act as toggles (remove if already present).
    if (this.hasCommand(sectId, command)) {
        var id = this.commandBlockId(sectId, command);
        jQuery(this.wym._doc).find('#' + id).remove();
        delete this.presentationInfo[id];
    } else {
        var newId = this.insertCommandBlock(sectId, command);
        this.registerSection(newId);
        this.presentationInfo[newId].push(command);
        this.updateStyleDisplay(newId);
    }
    this.updateClassListItem(btn, command);
};

PresentationControls.prototype.cleanPresentationInfo = function() {
    // clear out orphaned items
    var orphaned = [];
    for (var key in this.presentationInfo) {
        var sel = "#" + key;
        if (!jQuery(this.wym._doc).find(sel).is(sel)) {
            orphaned.push(key);
        }
    }
    for (var i = 0; i < orphaned.length; i++) {
        delete this.presentationInfo[orphaned[i]];
    }
};

// ---- Error box -----

PresentationControls.prototype.clearError = function() {
    this.errorBox.empty();
};

PresentationControls.prototype.showError = function(message) {
    this.clearError();
    this.errorBox.append(this.escapeHtml(message));
};
// ---- Preview ---

PresentationControls.prototype.showPreview = function() {
    this.prepareData();
    var self = this;
    jQuery.post(this.opts.previewUrl, {'html': self.wym.xhtml(),
                                       'presentation': JSON.stringify(this.presentationInfo)
                                      },
                function(data) {
                    self.withGoodData(data,
                        function(value) {
                            var btn = self.previewButton;
                            var box = self.previewBox;
                            var pos = btn.offset();
                            box.find(".content").html(value.html);
                            var height = box.outerHeight();
                            box.css("top", pos.top - height - 20).css("left", pos.left);
                            box.show();
                        });
                }, "json");
    return false;
};

PresentationControls.prototype.showStyles = function(show) {
    if (show) {
        jQuery(this.wym._doc).find('#presmodestyles').remove();
        jQuery(this.wym._iframe.ownerDocument).find('#presmodestyles').remove();
        this.showStylesButton.attr('value', 'Hide styles');
        // Fix height of list of classes.
        var h = jQuery(" .wym_area_main").outerHeight() -
            jQuery(this.wym._options.containersSelector).outerHeight() -
            jQuery(this.wym._options.layoutCommandsSelector).outerHeight() -
            20; // fudge factor, padding related?
        jQuery(this.wym._options.classesSelector).height(h);


    } else {
        jQuery('<style rel="stylesheet" type="text/css" id="presmodestyles">' +
               'p.secommand { display:none; } ' +
               '*:before    { display: none!important; } ' +
               '*:after     { top: 0!important; } ' +
               '</style>').appendTo(jQuery(this.wym._doc).find("head"));
        jQuery('<style rel="stylesheet" type="text/css" id="presmodestyles">' +
               '.wym_layout_commands, .wym_classes  {display: none!important;} ' +
               '</style>').appendTo(jQuery(this.wym._iframe.ownerDocument).find("head"));
        this.showStylesButton.attr('value', 'Show styles');
    }
};

// ---- WYMeditor plugin definition ----

// The actual WYMeditor plugin:
WYMeditor.editor.prototype.semantic = function(options) {
    var wym = this;
    var c = new PresentationControls(wym, options);
};
