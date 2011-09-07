WYMeditor.SKINS['semanticeditor'] = {

    init: function(wym) {

        // render 'classes' as a panel, but remove contents
        // (will be added later dynamically)
        jQuery(wym._box).find(wym._options.classesSelector)
	    .addClass("wym_panel").find("li").remove();

        // add an additional box for 'commands'.
        // This will be filled in later in the 'semantic' plugin.
        wym._options.layoutCommandsSelector = ".wym_layout_commands";
        jQuery(wym._box).find(wym._options.classesSelector).before('<div class="wym_layout_commands wym_section wym_panel"><h2>Rows & columns</h2><ul></ul></div>');

        //render following sections as buttons
        jQuery(wym._box).find(wym._options.toolsSelector)
          .addClass("wym_buttons");

        //render following sections as dropdown menus
        jQuery(wym._box).find(wym._options.containersSelector)
          .addClass("wym_panel")
          .find(WYMeditor.H2);

        // auto add some margin to the main area sides if left area
        // or right area are not empty (if they contain sections)
        jQuery(wym._box).find("div.wym_area_right ul")
          .parents("div.wym_area_right").show()
          .parents(wym._options.boxSelector)
          .find("div.wym_area_main")
          .css({"margin-right": "185px"});

        jQuery(wym._box).find("div.wym_area_left ul")
          .parents("div.wym_area_left").show()
          .parents(wym._options.boxSelector)
          .find("div.wym_area_main")
          .css({"margin-left": "155px"});

        //make hover work under IE < 7
        jQuery(wym._box).find(".wym_section").hover(function(){
          jQuery(this).addClass("hover");
        },function(){
          jQuery(this).removeClass("hover");
        });
    }
};
