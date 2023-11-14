/*! For license information please see fa6c2a7f.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[37232],{63207:function(t,e,n){n(65660),n(15112);var r=n(9672),i=n(87156),o=n(50856),a=n(48175);(0,r.k)({_template:o.d`
    <style>
      :host {
        @apply --layout-inline;
        @apply --layout-center-center;
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        @apply --iron-icon;
      }

      :host([hidden]) {
        display: none;
      }
    </style>
`,is:"iron-icon",properties:{icon:{type:String},theme:{type:String},src:{type:String},_meta:{value:a.XY.create("iron-meta",{type:"iconset"})}},observers:["_updateIcon(_meta, isAttached)","_updateIcon(theme, isAttached)","_srcChanged(src, isAttached)","_iconChanged(icon, isAttached)"],_DEFAULT_ICONSET:"icons",_iconChanged:function(t){var e=(t||"").split(":");this._iconName=e.pop(),this._iconsetName=e.pop()||this._DEFAULT_ICONSET,this._updateIcon()},_srcChanged:function(t){this._updateIcon()},_usesIconset:function(){return this.icon||!this.src},_updateIcon:function(){this._usesIconset()?(this._img&&this._img.parentNode&&(0,i.vz)(this.root).removeChild(this._img),""===this._iconName?this._iconset&&this._iconset.removeIcon(this):this._iconsetName&&this._meta&&(this._iconset=this._meta.byKey(this._iconsetName),this._iconset?(this._iconset.applyIcon(this,this._iconName,this.theme),this.unlisten(window,"iron-iconset-added","_updateIcon")):this.listen(window,"iron-iconset-added","_updateIcon"))):(this._iconset&&this._iconset.removeIcon(this),this._img||(this._img=document.createElement("img"),this._img.style.width="100%",this._img.style.height="100%",this._img.draggable=!1),this._img.src=this.src,(0,i.vz)(this.root).appendChild(this._img))}})},15112:function(t,e,n){n.d(e,{P:function(){return i}});n(48175);var r=n(9672);class i{constructor(t){i[" "](t),this.type=t&&t.type||"default",this.key=t&&t.key,t&&"value"in t&&(this.value=t.value)}get value(){var t=this.type,e=this.key;if(t&&e)return i.types[t]&&i.types[t][e]}set value(t){var e=this.type,n=this.key;e&&n&&(e=i.types[e]=i.types[e]||{},null==t?delete e[n]:e[n]=t)}get list(){if(this.type){var t=i.types[this.type];return t?Object.keys(t).map((function(t){return o[this.type][t]}),this):[]}}byKey(t){return this.key=t,this.value}}i[" "]=function(){},i.types={};var o=i.types;(0,r.k)({is:"iron-meta",properties:{type:{type:String,value:"default"},key:{type:String},value:{type:String,notify:!0},self:{type:Boolean,observer:"_selfChanged"},__meta:{type:Boolean,computed:"__computeMeta(type, key, value)"}},hostAttributes:{hidden:!0},__computeMeta:function(t,e,n){var r=new i({type:t,key:e});return void 0!==n&&n!==r.value?r.value=n:this.value!==r.value&&(this.value=r.value),r},get list(){return this.__meta&&this.__meta.list},_selfChanged:function(t){t&&(this.value=this)},byKey:function(t){return new i({type:this.type,key:t}).value}})},89194:function(t,e,n){n(48175),n(65660),n(70019);var r=n(9672),i=n(50856);(0,r.k)({_template:i.d`
    <style>
      :host {
        overflow: hidden; /* needed for text-overflow: ellipsis to work on ff */
        @apply --layout-vertical;
        @apply --layout-center-justified;
        @apply --layout-flex;
      }

      :host([two-line]) {
        min-height: var(--paper-item-body-two-line-min-height, 72px);
      }

      :host([three-line]) {
        min-height: var(--paper-item-body-three-line-min-height, 88px);
      }

      :host > ::slotted(*) {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      :host > ::slotted([secondary]) {
        @apply --paper-font-body1;

        color: var(--paper-item-body-secondary-color, var(--secondary-text-color));

        @apply --paper-item-body-secondary;
      }
    </style>

    <slot></slot>
`,is:"paper-item-body"})},23682:function(t,e,n){function r(t,e){if(e.length<t)throw new TypeError(t+" argument"+(t>1?"s":"")+" required, but only "+e.length+" present")}n.d(e,{Z:function(){return r}})},90394:function(t,e,n){function r(t){if(null===t||!0===t||!1===t)return NaN;var e=Number(t);return isNaN(e)?e:e<0?Math.ceil(e):Math.floor(e)}n.d(e,{Z:function(){return r}})},79021:function(t,e,n){n.d(e,{Z:function(){return a}});var r=n(90394),i=n(34327),o=n(23682);function a(t,e){(0,o.Z)(2,arguments);var n=(0,i.Z)(t),a=(0,r.Z)(e);return isNaN(a)?new Date(NaN):a?(n.setDate(n.getDate()+a),n):n}},59699:function(t,e,n){n.d(e,{Z:function(){return s}});var r=n(90394),i=n(39244),o=n(23682),a=36e5;function s(t,e){(0,o.Z)(2,arguments);var n=(0,r.Z)(e);return(0,i.Z)(t,n*a)}},39244:function(t,e,n){n.d(e,{Z:function(){return a}});var r=n(90394),i=n(34327),o=n(23682);function a(t,e){(0,o.Z)(2,arguments);var n=(0,i.Z)(t).getTime(),a=(0,r.Z)(e);return new Date(n+a)}},32182:function(t,e,n){n.d(e,{Z:function(){return a}});var r=n(90394),i=n(34327),o=n(23682);function a(t,e){(0,o.Z)(2,arguments);var n=(0,i.Z)(t),a=(0,r.Z)(e);if(isNaN(a))return new Date(NaN);if(!a)return n;var s=n.getDate(),u=new Date(n.getTime());return u.setMonth(n.getMonth()+a+1,0),s>=u.getDate()?u:(n.setFullYear(u.getFullYear(),u.getMonth(),s),n)}},4535:function(t,e,n){n.d(e,{Z:function(){return c}});var r=n(34327);function i(t){var e=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return e.setUTCFullYear(t.getFullYear()),t.getTime()-e.getTime()}var o=n(59429),a=n(23682),s=864e5;function u(t,e){var n=t.getFullYear()-e.getFullYear()||t.getMonth()-e.getMonth()||t.getDate()-e.getDate()||t.getHours()-e.getHours()||t.getMinutes()-e.getMinutes()||t.getSeconds()-e.getSeconds()||t.getMilliseconds()-e.getMilliseconds();return n<0?-1:n>0?1:n}function c(t,e){(0,a.Z)(2,arguments);var n=(0,r.Z)(t),c=(0,r.Z)(e),l=u(n,c),h=Math.abs(function(t,e){(0,a.Z)(2,arguments);var n=(0,o.Z)(t),r=(0,o.Z)(e),u=n.getTime()-i(n),c=r.getTime()-i(r);return Math.round((u-c)/s)}(n,c));n.setDate(n.getDate()-l*h);var f=l*(h-Number(u(n,c)===-l));return 0===f?0:f}},93752:function(t,e,n){n.d(e,{Z:function(){return o}});var r=n(34327),i=n(23682);function o(t){(0,i.Z)(1,arguments);var e=(0,r.Z)(t);return e.setHours(23,59,59,999),e}},70390:function(t,e,n){n.d(e,{Z:function(){return i}});var r=n(93752);function i(){return(0,r.Z)(Date.now())}},47538:function(t,e,n){function r(){var t=new Date,e=t.getFullYear(),n=t.getMonth(),r=t.getDate(),i=new Date(0);return i.setFullYear(e,n,r-1),i.setHours(23,59,59,999),i}n.d(e,{Z:function(){return r}})},59429:function(t,e,n){n.d(e,{Z:function(){return o}});var r=n(34327),i=n(23682);function o(t){(0,i.Z)(1,arguments);var e=(0,r.Z)(t);return e.setHours(0,0,0,0),e}},27088:function(t,e,n){n.d(e,{Z:function(){return i}});var r=n(59429);function i(){return(0,r.Z)(Date.now())}},83008:function(t,e,n){function r(){var t=new Date,e=t.getFullYear(),n=t.getMonth(),r=t.getDate(),i=new Date(0);return i.setFullYear(e,n,r-1),i.setHours(0,0,0,0),i}n.d(e,{Z:function(){return r}})},34327:function(t,e,n){n.d(e,{Z:function(){return o}});var r=n(76775),i=n(23682);function o(t){(0,i.Z)(1,arguments);var e=Object.prototype.toString.call(t);return t instanceof Date||"object"===(0,r.Z)(t)&&"[object Date]"===e?new Date(t.getTime()):"number"==typeof t||"[object Number]"===e?new Date(t):("string"!=typeof t&&"[object String]"!==e||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments"),console.warn((new Error).stack)),new Date(NaN))}},21560:function(t,e,n){n.d(e,{ZH:function(){return l},MT:function(){return o},U2:function(){return u},RV:function(){return i},t8:function(){return c}});var r=function(){if(!(!navigator.userAgentData&&/Safari\//.test(navigator.userAgent)&&!/Chrom(e|ium)\//.test(navigator.userAgent))||!indexedDB.databases)return Promise.resolve();let t;return new Promise((e=>{const n=()=>indexedDB.databases().finally(e);t=setInterval(n,100),n()})).finally((()=>clearInterval(t)))};function i(t){return new Promise(((e,n)=>{t.oncomplete=t.onsuccess=()=>e(t.result),t.onabort=t.onerror=()=>n(t.error)}))}function o(t,e){const n=r().then((()=>{const n=indexedDB.open(t);return n.onupgradeneeded=()=>n.result.createObjectStore(e),i(n)}));return(t,r)=>n.then((n=>r(n.transaction(e,t).objectStore(e))))}let a;function s(){return a||(a=o("keyval-store","keyval")),a}function u(t,e=s()){return e("readonly",(e=>i(e.get(t))))}function c(t,e,n=s()){return n("readwrite",(n=>(n.put(e,t),i(n.transaction))))}function l(t=s()){return t("readwrite",(t=>(t.clear(),i(t.transaction))))}},76775:function(t,e,n){function r(t){return r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},r(t)}n.d(e,{Z:function(){return r}})}}]);
//# sourceMappingURL=fa6c2a7f.js.map