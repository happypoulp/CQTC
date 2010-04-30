/***********************************
**  Utility
***********************************/

function log(msg)
{
    if (typeof console != 'undefined')
    {
        console.log(msg);
    }
    else
    {
        alert(msg);
    }
}

/***********************************
**  JQuery extension
***********************************/

jQuery.fn.extend({
    getClassParam: function(param)
    {
        try
        {
            var regex = new RegExp(param + "_([A-Za-z0-9/:?&._-]+)");
            var match = regex.exec(this.get(0).className);

            if(match)
            {
                return match[1];
            }
        }
        catch(e){}

        return false;
    }
});

/***********************************
**  Poodding js essential
***********************************/

var Essential = {
    handleLink: function(link)
    {
        var linkObj = $(link);
        var targetLabel = linkObj.getClassParam('target');
        var targetElement = linkObj.closest('.'+targetLabel).eq(0);
        var targetId = targetElement.getClassParam('id');
        var newTag = linkObj.getClassParam('newtag');
        var mode = linkObj.getClassParam('mode');
        var action = linkObj.get(0).href;

        $.get
        (
            action,
            null,
            function(html)
            {
                var placeholderSelector = '.' + targetLabel + '.id_' + targetId;
                var elementBackup = null;
                var newElement = $(html);

                switch(mode)
                {
                    case 'new':
                    case 'edit':
                        elementBackup = targetElement.replaceWith(newElement);
                    break;
                    case 'delete':
                        if (confirm('Are you sure you want to delete this?'))
                        {
                            Essential.handleDeleteAction(action);
                        }
                        newElement = null;
                    break;
                }

                if (newElement)
                {
                    Essential.handleNewElement(newElement, newTag, action, placeholderSelector, elementBackup);
                }
            }
        );
    },
    handleDeleteAction: function(action)
    {
        $.post
        (
            action,
            null,
            function(result)
            {
                var newElement = $(result.html);
                if (result.success)
                {
                    // Replace the element matching the one we received by the new one
                    $('.'+newElement.get(0).className.replace(new RegExp(' ', 'g'), '.')).replaceWith(newElement);
                }
            }, 'json'
        );
    },
    handleNewElement: function(newElement, newTag, action, placeholderSelector, elementBackup)
    {
        switch(newTag)
        {
            case 'form':
                Essential.form_focus(newElement);
                Essential.prepareForm(newElement, action, elementBackup);
            break;
            default:
                // handle other possibilities here
            break;
        }
    },
    prepareForm: function(form, action, elementBackup)
    {
        $(form).data('backup', { html: elementBackup });

        $(form).submit(function(event)
        {
            event.preventDefault();
            $.post
            (
                action,
                $(form).serialize(),
                function(result)
                {
                    var newElement = $(result.html);
                    if (!result.success)
                    {
                        newElement.data('backup', { html: elementBackup });
                        Essential.prepareForm(newElement, action, elementBackup);
                    }
                    $(form).replaceWith(newElement);
                    Essential.form_focus(newElement);
                }, 'json'
            );
        });
    },
    // TODO
    handleForm: function(form, action, elementBackup)
    {
    },
    backupElement: function(source, parent)
    {
        if (source && parent)
        {
            el = $(source).closest(parent);
            var backup = el && el.data('backup') && el.data('backup').html ? el.data('backup').html : false;
            if (backup)
            {
                el.replaceWith(backup);
            }
        }
    },
    url_switcher: function()
    {
        $('.url_switch').change(function(){document.location = this.value;});
    },
    form_focus: function(container)
    {
        if (container && $(container).get(0).tagName != 'FORM')
        {
            var forms = $(container).find('form.focus');
        }
        else
        {
            var forms = container ? $(container) : $('form.focus');
        }

        forms.each(function(index, item)
        {
            $(item).find('input[name="'+$(item).getClassParam('focus')+'"]').focus();
            $(item).find('textarea[name="'+$(item).getClassParam('focus')+'"]').focus();
        });
    },
    init: function()
    {
        // On DOM Ready
        $(function()
        {
            Essential.url_switcher();
            Essential.form_focus();
        });
    }

}

Essential.init();