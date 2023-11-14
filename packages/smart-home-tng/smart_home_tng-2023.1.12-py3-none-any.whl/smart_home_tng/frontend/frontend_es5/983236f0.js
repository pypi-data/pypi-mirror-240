/*! For license information please see 983236f0.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[79230],{18601:function(t,i,n){n.d(i,{Wg:function(){return c},qN:function(){return r.q}});var e,o,a=n(43204),s=n(36924),r=n(78220);const l=null!==(o=null===(e=window.ShadyDOM)||void 0===e?void 0:e.inUse)&&void 0!==o&&o;class c extends r.H{constructor(){super(...arguments),this.disabled=!1,this.containingForm=null,this.formDataListener=t=>{this.disabled||this.setFormData(t.formData)}}findFormElement(){if(!this.shadowRoot||l)return null;const t=this.getRootNode().querySelectorAll("form");for(const i of Array.from(t))if(i.contains(this))return i;return null}connectedCallback(){var t;super.connectedCallback(),this.containingForm=this.findFormElement(),null===(t=this.containingForm)||void 0===t||t.addEventListener("formdata",this.formDataListener)}disconnectedCallback(){var t;super.disconnectedCallback(),null===(t=this.containingForm)||void 0===t||t.removeEventListener("formdata",this.formDataListener),this.containingForm=null}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(t=>{this.dispatchEvent(new Event("change",t))}))}}c.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,a.__decorate)([(0,s.Cb)({type:Boolean})],c.prototype,"disabled",void 0)},14114:function(t,i,n){n.d(i,{P:function(){return e}});const e=t=>(i,n)=>{if(i.constructor._observers){if(!i.constructor.hasOwnProperty("_observers")){const t=i.constructor._observers;i.constructor._observers=new Map,t.forEach(((t,n)=>i.constructor._observers.set(n,t)))}}else{i.constructor._observers=new Map;const t=i.updated;i.updated=function(i){t.call(this,i),i.forEach(((t,i)=>{const n=this.constructor._observers.get(i);void 0!==n&&n.call(this,this[i],t)}))}}i.constructor._observers.set(n,t)}},54444:function(t,i,n){n(48175);var e=n(9672),o=n(87156),a=n(50856);(0,e.k)({_template:a.d`
    <style>
      :host {
        display: block;
        position: absolute;
        outline: none;
        z-index: 1002;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;
        cursor: default;
      }

      #tooltip {
        display: block;
        outline: none;
        @apply --paper-font-common-base;
        font-size: 10px;
        line-height: 1;
        background-color: var(--paper-tooltip-background, #616161);
        color: var(--paper-tooltip-text-color, white);
        padding: 8px;
        border-radius: 2px;
        @apply --paper-tooltip;
      }

      @keyframes keyFrameScaleUp {
        0% {
          transform: scale(0.0);
        }
        100% {
          transform: scale(1.0);
        }
      }

      @keyframes keyFrameScaleDown {
        0% {
          transform: scale(1.0);
        }
        100% {
          transform: scale(0.0);
        }
      }

      @keyframes keyFrameFadeInOpacity {
        0% {
          opacity: 0;
        }
        100% {
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
      }

      @keyframes keyFrameFadeOutOpacity {
        0% {
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
        100% {
          opacity: 0;
        }
      }

      @keyframes keyFrameSlideDownIn {
        0% {
          transform: translateY(-2000px);
          opacity: 0;
        }
        10% {
          opacity: 0.2;
        }
        100% {
          transform: translateY(0);
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
      }

      @keyframes keyFrameSlideDownOut {
        0% {
          transform: translateY(0);
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
        10% {
          opacity: 0.2;
        }
        100% {
          transform: translateY(-2000px);
          opacity: 0;
        }
      }

      .fade-in-animation {
        opacity: 0;
        animation-delay: var(--paper-tooltip-delay-in, 500ms);
        animation-name: keyFrameFadeInOpacity;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-in, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .fade-out-animation {
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 0ms);
        animation-name: keyFrameFadeOutOpacity;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .scale-up-animation {
        transform: scale(0);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-in, 500ms);
        animation-name: keyFrameScaleUp;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-in, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .scale-down-animation {
        transform: scale(1);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameScaleDown;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .slide-down-animation {
        transform: translateY(-2000px);
        opacity: 0;
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameSlideDownIn;
        animation-iteration-count: 1;
        animation-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .slide-down-animation-out {
        transform: translateY(0);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameSlideDownOut;
        animation-iteration-count: 1;
        animation-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .cancel-animation {
        animation-delay: -30s !important;
      }

      /* Thanks IE 10. */

      .hidden {
        display: none !important;
      }
    </style>

    <div id="tooltip" class="hidden">
      <slot></slot>
    </div>
`,is:"paper-tooltip",hostAttributes:{role:"tooltip",tabindex:-1},properties:{for:{type:String,observer:"_findTarget"},manualMode:{type:Boolean,value:!1,observer:"_manualModeChanged"},position:{type:String,value:"bottom"},fitToVisibleBounds:{type:Boolean,value:!1},offset:{type:Number,value:14},marginTop:{type:Number,value:14},animationDelay:{type:Number,value:500,observer:"_delayChange"},animationEntry:{type:String,value:""},animationExit:{type:String,value:""},animationConfig:{type:Object,value:function(){return{entry:[{name:"fade-in-animation",node:this,timing:{delay:0}}],exit:[{name:"fade-out-animation",node:this}]}}},_showing:{type:Boolean,value:!1}},listeners:{webkitAnimationEnd:"_onAnimationEnd"},get target(){var t=(0,o.vz)(this).parentNode,i=(0,o.vz)(this).getOwnerRoot();return this.for?(0,o.vz)(i).querySelector("#"+this.for):t.nodeType==Node.DOCUMENT_FRAGMENT_NODE?i.host:t},attached:function(){this._findTarget()},detached:function(){this.manualMode||this._removeListeners()},playAnimation:function(t){"entry"===t?this.show():"exit"===t&&this.hide()},cancelAnimation:function(){this.$.tooltip.classList.add("cancel-animation")},show:function(){if(!this._showing){if(""===(0,o.vz)(this).textContent.trim()){for(var t=!0,i=(0,o.vz)(this).getEffectiveChildNodes(),n=0;n<i.length;n++)if(""!==i[n].textContent.trim()){t=!1;break}if(t)return}this._showing=!0,this.$.tooltip.classList.remove("hidden"),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.updatePosition(),this._animationPlaying=!0,this.$.tooltip.classList.add(this._getAnimationType("entry"))}},hide:function(){if(this._showing){if(this._animationPlaying)return this._showing=!1,void this._cancelAnimation();this._onAnimationFinish(),this._showing=!1,this._animationPlaying=!0}},updatePosition:function(){if(this._target&&this.offsetParent){var t=this.offset;14!=this.marginTop&&14==this.offset&&(t=this.marginTop);var i,n,e=this.offsetParent.getBoundingClientRect(),o=this._target.getBoundingClientRect(),a=this.getBoundingClientRect(),s=(o.width-a.width)/2,r=(o.height-a.height)/2,l=o.left-e.left,c=o.top-e.top;switch(this.position){case"top":i=l+s,n=c-a.height-t;break;case"bottom":i=l+s,n=c+o.height+t;break;case"left":i=l-a.width-t,n=c+r;break;case"right":i=l+o.width+t,n=c+r}this.fitToVisibleBounds?(e.left+i+a.width>window.innerWidth?(this.style.right="0px",this.style.left="auto"):(this.style.left=Math.max(0,i)+"px",this.style.right="auto"),e.top+n+a.height>window.innerHeight?(this.style.bottom=e.height-c+t+"px",this.style.top="auto"):(this.style.top=Math.max(-e.top,n)+"px",this.style.bottom="auto")):(this.style.left=i+"px",this.style.top=n+"px")}},_addListeners:function(){this._target&&(this.listen(this._target,"mouseenter","show"),this.listen(this._target,"focus","show"),this.listen(this._target,"mouseleave","hide"),this.listen(this._target,"blur","hide"),this.listen(this._target,"tap","hide")),this.listen(this.$.tooltip,"animationend","_onAnimationEnd"),this.listen(this,"mouseenter","hide")},_findTarget:function(){this.manualMode||this._removeListeners(),this._target=this.target,this.manualMode||this._addListeners()},_delayChange:function(t){500!==t&&this.updateStyles({"--paper-tooltip-delay-in":t+"ms"})},_manualModeChanged:function(){this.manualMode?this._removeListeners():this._addListeners()},_cancelAnimation:function(){this.$.tooltip.classList.remove(this._getAnimationType("entry")),this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.add("hidden")},_onAnimationFinish:function(){this._showing&&(this.$.tooltip.classList.remove(this._getAnimationType("entry")),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.add(this._getAnimationType("exit")))},_onAnimationEnd:function(){this._animationPlaying=!1,this._showing||(this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.$.tooltip.classList.add("hidden"))},_getAnimationType:function(t){if("entry"===t&&""!==this.animationEntry)return this.animationEntry;if("exit"===t&&""!==this.animationExit)return this.animationExit;if(this.animationConfig[t]&&"string"==typeof this.animationConfig[t][0].name){if(this.animationConfig[t][0].timing&&this.animationConfig[t][0].timing.delay&&0!==this.animationConfig[t][0].timing.delay){var i=this.animationConfig[t][0].timing.delay;"entry"===t?this.updateStyles({"--paper-tooltip-delay-in":i+"ms"}):"exit"===t&&this.updateStyles({"--paper-tooltip-delay-out":i+"ms"})}return this.animationConfig[t][0].name}},_removeListeners:function(){this._target&&(this.unlisten(this._target,"mouseenter","show"),this.unlisten(this._target,"focus","show"),this.unlisten(this._target,"mouseleave","hide"),this.unlisten(this._target,"blur","hide"),this.unlisten(this._target,"tap","hide")),this.unlisten(this.$.tooltip,"animationend","_onAnimationEnd"),this.unlisten(this,"mouseenter","hide")}})},3239:function(t,i,n){function e(t){if(!t||"object"!=typeof t)return t;if("[object Date]"==Object.prototype.toString.call(t))return new Date(t.getTime());if(Array.isArray(t))return t.map(e);var i={};return Object.keys(t).forEach((function(n){i[n]=e(t[n])})),i}n.d(i,{Z:function(){return e}})},93217:function(t,i,n){n.d(i,{Ud:function(){return h}});const e=Symbol("Comlink.proxy"),o=Symbol("Comlink.endpoint"),a=Symbol("Comlink.releaseProxy"),s=Symbol("Comlink.finalizer"),r=Symbol("Comlink.thrown"),l=t=>"object"==typeof t&&null!==t||"function"==typeof t,c=new Map([["proxy",{canHandle:t=>l(t)&&t[e],serialize(t){const{port1:i,port2:n}=new MessageChannel;return u(t,i),[n,[n]]},deserialize(t){return t.start(),h(t)}}],["throw",{canHandle:t=>l(t)&&r in t,serialize({value:t}){let i;return i=t instanceof Error?{isError:!0,value:{message:t.message,name:t.name,stack:t.stack}}:{isError:!1,value:t},[i,[]]},deserialize(t){if(t.isError)throw Object.assign(new Error(t.value.message),t.value);throw t.value}}]]);function u(t,i=globalThis,n=["*"]){i.addEventListener("message",(function o(a){if(!a||!a.data)return;if(!function(t,i){for(const n of t){if(i===n||"*"===n)return!0;if(n instanceof RegExp&&n.test(i))return!0}return!1}(n,a.origin))return void console.warn(`Invalid origin '${a.origin}' for comlink proxy`);const{id:l,type:c,path:h}=Object.assign({path:[]},a.data),d=(a.data.argumentList||[]).map(A);let m;try{const i=h.slice(0,-1).reduce(((t,i)=>t[i]),t),n=h.reduce(((t,i)=>t[i]),t);switch(c){case"GET":m=n;break;case"SET":i[h.slice(-1)[0]]=A(a.data.value),m=!0;break;case"APPLY":m=n.apply(i,d);break;case"CONSTRUCT":m=function(t){return Object.assign(t,{[e]:!0})}(new n(...d));break;case"ENDPOINT":{const{port1:i,port2:n}=new MessageChannel;u(t,n),m=function(t,i){return _.set(t,i),t}(i,[i])}break;case"RELEASE":m=void 0;break;default:return}}catch(f){m={value:f,[r]:0}}Promise.resolve(m).catch((t=>({value:t,[r]:0}))).then((n=>{const[e,a]=b(n);i.postMessage(Object.assign(Object.assign({},e),{id:l}),a),"RELEASE"===c&&(i.removeEventListener("message",o),p(i),s in t&&"function"==typeof t[s]&&t[s]())})).catch((t=>{const[n,e]=b({value:new TypeError("Unserializable return value"),[r]:0});i.postMessage(Object.assign(Object.assign({},n),{id:l}),e)}))})),i.start&&i.start()}function p(t){(function(t){return"MessagePort"===t.constructor.name})(t)&&t.close()}function h(t,i){return g(t,[],i)}function d(t){if(t)throw new Error("Proxy has been released and is not useable")}function m(t){return w(t,{type:"RELEASE"}).then((()=>{p(t)}))}const f=new WeakMap,y="FinalizationRegistry"in globalThis&&new FinalizationRegistry((t=>{const i=(f.get(t)||0)-1;f.set(t,i),0===i&&m(t)}));function g(t,i=[],n=function(){}){let e=!1;const s=new Proxy(n,{get(n,o){if(d(e),o===a)return()=>{!function(t){y&&y.unregister(t)}(s),m(t),e=!0};if("then"===o){if(0===i.length)return{then:()=>s};const n=w(t,{type:"GET",path:i.map((t=>t.toString()))}).then(A);return n.then.bind(n)}return g(t,[...i,o])},set(n,o,a){d(e);const[s,r]=b(a);return w(t,{type:"SET",path:[...i,o].map((t=>t.toString())),value:s},r).then(A)},apply(n,a,s){d(e);const r=i[i.length-1];if(r===o)return w(t,{type:"ENDPOINT"}).then(A);if("bind"===r)return g(t,i.slice(0,-1));const[l,c]=v(s);return w(t,{type:"APPLY",path:i.map((t=>t.toString())),argumentList:l},c).then(A)},construct(n,o){d(e);const[a,s]=v(o);return w(t,{type:"CONSTRUCT",path:i.map((t=>t.toString())),argumentList:a},s).then(A)}});return function(t,i){const n=(f.get(i)||0)+1;f.set(i,n),y&&y.register(t,i,t)}(s,t),s}function v(t){const i=t.map(b);return[i.map((t=>t[0])),(n=i.map((t=>t[1])),Array.prototype.concat.apply([],n))];var n}const _=new WeakMap;function b(t){for(const[i,n]of c)if(n.canHandle(t)){const[e,o]=n.serialize(t);return[{type:"HANDLER",name:i,value:e},o]}return[{type:"RAW",value:t},_.get(t)||[]]}function A(t){switch(t.type){case"HANDLER":return c.get(t.name).deserialize(t.value);case"RAW":return t.value}}function w(t,i,n){return new Promise((e=>{const o=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");t.addEventListener("message",(function i(n){n.data&&n.data.id&&n.data.id===o&&(t.removeEventListener("message",i),e(n.data))})),t.start&&t.start(),t.postMessage(Object.assign({id:o},i),n)}))}},19596:function(t,i,n){n.d(i,{sR:function(){return p}});var e=n(81563),o=n(38941);const a=(t,i)=>{var n,e;const o=t._$AN;if(void 0===o)return!1;for(const s of o)null===(e=(n=s)._$AO)||void 0===e||e.call(n,i,!1),a(s,i);return!0},s=t=>{let i,n;do{if(void 0===(i=t._$AM))break;n=i._$AN,n.delete(t),t=i}while(0===(null==n?void 0:n.size))},r=t=>{for(let i;i=t._$AM;t=i){let n=i._$AN;if(void 0===n)i._$AN=n=new Set;else if(n.has(t))break;n.add(t),u(i)}};function l(t){void 0!==this._$AN?(s(this),this._$AM=t,r(this)):this._$AM=t}function c(t,i=!1,n=0){const e=this._$AH,o=this._$AN;if(void 0!==o&&0!==o.size)if(i)if(Array.isArray(e))for(let r=n;r<e.length;r++)a(e[r],!1),s(e[r]);else null!=e&&(a(e,!1),s(e));else a(this,t)}const u=t=>{var i,n,e,a;t.type==o.pX.CHILD&&(null!==(i=(e=t)._$AP)&&void 0!==i||(e._$AP=c),null!==(n=(a=t)._$AQ)&&void 0!==n||(a._$AQ=l))};class p extends o.Xe{constructor(){super(...arguments),this._$AN=void 0}_$AT(t,i,n){super._$AT(t,i,n),r(this),this.isConnected=t._$AU}_$AO(t,i=!0){var n,e;t!==this.isConnected&&(this.isConnected=t,t?null===(n=this.reconnected)||void 0===n||n.call(this):null===(e=this.disconnected)||void 0===e||e.call(this)),i&&(a(this,t),s(this))}setValue(t){if((0,e.OR)(this._$Ct))this._$Ct._$AI(t,this);else{const i=[...this._$Ct._$AH];i[this._$Ci]=t,this._$Ct._$AI(i,this,0)}}disconnected(){}reconnected(){}}},81563:function(t,i,n){n.d(i,{E_:function(){return y},OR:function(){return l},_Y:function(){return u},dZ:function(){return r},fk:function(){return p},hN:function(){return s},hl:function(){return d},i9:function(){return m},pt:function(){return a},ws:function(){return f}});var e=n(15304);const{I:o}=e._$LH,a=t=>null===t||"object"!=typeof t&&"function"!=typeof t,s=(t,i)=>void 0===i?void 0!==(null==t?void 0:t._$litType$):(null==t?void 0:t._$litType$)===i,r=t=>{var i;return null!=(null===(i=null==t?void 0:t._$litType$)||void 0===i?void 0:i.h)},l=t=>void 0===t.strings,c=()=>document.createComment(""),u=(t,i,n)=>{var e;const a=t._$AA.parentNode,s=void 0===i?t._$AB:i._$AA;if(void 0===n){const i=a.insertBefore(c(),s),e=a.insertBefore(c(),s);n=new o(i,e,t,t.options)}else{const i=n._$AB.nextSibling,o=n._$AM,r=o!==t;if(r){let i;null===(e=n._$AQ)||void 0===e||e.call(n,t),n._$AM=t,void 0!==n._$AP&&(i=t._$AU)!==o._$AU&&n._$AP(i)}if(i!==s||r){let t=n._$AA;for(;t!==i;){const i=t.nextSibling;a.insertBefore(t,s),t=i}}}return n},p=(t,i,n=t)=>(t._$AI(i,n),t),h={},d=(t,i=h)=>t._$AH=i,m=t=>t._$AH,f=t=>{var i;null===(i=t._$AP)||void 0===i||i.call(t,!1,!0);let n=t._$AA;const e=t._$AB.nextSibling;for(;n!==e;){const t=n.nextSibling;n.remove(),n=t}},y=t=>{t._$AR()}},57835:function(t,i,n){n.d(i,{XM:function(){return e.XM},Xe:function(){return e.Xe},pX:function(){return e.pX}});var e=n(38941)}}]);
//# sourceMappingURL=983236f0.js.map