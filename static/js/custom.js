/*------------------------------------------------------
 Author : www.webthemez.com
 License: Commons Attribution 3.0
 http://creativecommons.org/licenses/by/3.0/
 ---------------------------------------------------------  */

(function ($) {
    "use strict";
    var mainApp = {

        initFunction: function () {
            /*MENU 
             ------------------------------------*/
            $('#main-menu').metisMenu();
        },

        initialization: function () {
            mainApp.initFunction();

        }

    }
    // Initializing ///

    $(document).ready(function () {
        mainApp.initFunction();
    });

}(jQuery));

SL = {};

+function (SL, $) {


    SL.del_item = function (url) {
        if (confirm('你确定要删除吗？')) {
            $.get(url, function (data) {
                if (data.code == 1)
                    window.location.reload();
                else
                    alert('出错了。。。' + data.code);
            });
        }
    }

    SL.modal_update_item = function (url, args) {
        $.post(url, args, function (data) {
                if (data.code == 1) {
                    window.location.reload();
                }
                else
                    alert(data.msg);
            }
        );
    }

    SL.modal_add_item = function (url, args) {
        $.post(url, args,
            function (data) {
                if (data.code == 1) {
                    window.location.reload();
                }
                else
                    alert(data.msg);
            }
        );
    }

    SL.upload_icon = function (imgid, formid) {
        var option = {
            url: '/madmin/api/upload',
            success: function (data) {
                $('#' + imgid)[0].src = data.url;
            }
        }
        $('#' + formid).ajaxSubmit(option);
    }


    SL.page_add_item = function (url,args,alertid) {
            $.post(url, args,
                function (data) {
                    if (data.code == 1) {
                        alertid.modal('show');
                        setTimeout(function () {
                            alertid.modal('hide');
                        }, 1000);
                    }
                    else
                        alert(data.msg);
                }
            );
    }


}(SL, $);
