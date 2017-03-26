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
}(SL, $);
