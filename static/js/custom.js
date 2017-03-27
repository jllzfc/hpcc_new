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


    SL.dialog = function () {
        var html = "<div class='dialog-me'>" +
            "<div class='title'>我是标题</div>" +
            "<div class='line'></div>" +
            "<div class='content'>afdsffasfsafsadfsdf</div>" +
            "<div class='bottom'>" +
            "<div class='bottom-line'></div> " +
            "<div class='bottom-button'>我是底部</div>" +
            "</div>" +
            "</div>";
        $(document.body).append(html);
    }

    SL.close_dialog = function () {
        $('.dialog-me').remove();
    }

    SL.set_menu = function (menu_name) {
        $.get('/main/api/set_menu_status?menu_name=' + menu_name, function (data) {
            if (data.code == 1) {
                var html_str = '';
                for (var i = 0; i < data.data.length; i++) {
                    html_str += '<li> <a class="' + data.data[i].class_ + '" href="' + data.data[i].href + '"><i class="fa fa-users"></i> ' + data.data[i].menu_name + '</a> </li>';
                }
                $('#main-menu').html(html_str);
            }
        })
    }

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

    SL.modal_update_item = function(url, args) {
        $.post(url, args, function (data) {
                if (data.code == 1) {
                    window.location.reload();
                }
                else
                    alert(data.msg);
            }
        );
    }

    SL.modal_add_item = function(url,args) {
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

    SL.upload_icon=function(imgid, formid) {
        var option = {
            url: '/madmin/api/upload',
            success: function (data) {
                $('#' + imgid)[0].src = data.url;
            }
        }
        $('#' + formid).ajaxSubmit(option);
    }


}(SL, $);
