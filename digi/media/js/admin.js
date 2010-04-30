/***********************************
**  Poodding js admin miscellaneous
***********************************/

var Admin = {
    // Grid is shown using SHIFT+G shortcut
    grid_handler: function()
    {
        var shift = false;

        $(document).keyup(function (e)
        {
            if(e.which == 16)
            {
                shift = false;
            }
        }).keydown(function (e)
        {
            if (['input', 'textarea'].indexOf(e.target.tagName.toLowerCase()) == -1)
            {
                if(e.which == 16)
                {
                    shift = true;
                }
                if(e.which == 71 && shift == true)
                {
                    if ($('div#poo_grid').length)
                    {
                        $('#poo_grid').remove();
                    }
                    else
                    {
                        $('body').append('<div id="poo_grid"><div id="poo_grid_inner"></div></div>');
                        $('#poo_grid').css({height: $('#wrapper').height()});
                    }
                    return false;
                }
            }
        });
    },
    init: function()
    {
        // On DOM Ready
        $(function()
        {
            Admin.grid_handler();
        });
    }

}

Admin.init();