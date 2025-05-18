// ==UserScript==
// @name         Fullscreen Shortcut
// @namespace    https://greasyfork.org/users/673298
// @version      1.2.4
// @author       Fingalzzz
// @description  Add a shortcut to enable fullscreen mode of several streaming-media websites
// @homepage     https://greasyfork.org/en/scripts/408194-fullscreen-shortcut
// @supportURL   https://greasyfork.org/en/scripts/408194-fullscreen-shortcut
// @updateURL    https://raw.githubusercontent.com/Fingalzzz/scripts/master/Tampermonkey/fullscreen.js
// @downloadURL  https://raw.githubusercontent.com/Fingalzzz/scripts/master/Tampermonkey/fullscreen.js
// @match        https://www.bilibili.com/video/*
// @match        https://www.bilibili.com/bangumi/play/*
// @match        https://www.iqiyi.com/*
// @match        https://v.qq.com/x/*
// @match        https://www.youtube.com/*
// @match        https://v.youku.com/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    const shortcut = 'Backslash';

    document.addEventListener('keydown', (e) => {
        //if (e.ctrlKey && e.key === shortcut) {
        if (e.code === shortcut) {
            var selector = null;
            var btn = null;
            var link = window.location.href;
            if (link.includes("bilibili.com/bangumi")) {
                selector = ".bpx-player-ctrl-btn.bpx-player-ctrl-full";
            } else if (link.includes("bilibili.com/video")) {
                selector = ".bpx-player-ctrl-btn.bpx-player-ctrl-full";
            } else if (link.includes('iqiyi.com')) {
                selector = ".iqp-btn.iqp-btn-fullscreen";
            } else if (link.includes('v.qq.com')) {
                selector = ".txp_btn.txp_btn_fullscreen";
            } else if (link.includes('youtube.com')) {
                selector = ".ytp-fullscreen-button.ytp-button";
            } else if (link.includes('v.youku.com')) {
                // Youku use different button to enable and exit fullscreen
                // so we need to check whether button we need now.
                selector = document.fullscreen? ".iconfont.icon-exit-fullscreen":".iconfont.icon-fullscreen"
            }
            btn = document.querySelector(selector);
            btn.click();
        }
    })

})();

