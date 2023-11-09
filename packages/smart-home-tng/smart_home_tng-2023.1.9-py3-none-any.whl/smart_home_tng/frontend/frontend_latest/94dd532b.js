/*! For license information please see 94dd532b.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[49540],{18601:(t,i,e)=>{e.d(i,{Wg:()=>p,qN:()=>r.q});var n,a,o=e(43204),s=e(33310),r=e(78220);const l=null!==(a=null===(n=window.ShadyDOM)||void 0===n?void 0:n.inUse)&&void 0!==a&&a;class p extends r.H{constructor(){super(...arguments),this.disabled=!1,this.containingForm=null,this.formDataListener=t=>{this.disabled||this.setFormData(t.formData)}}findFormElement(){if(!this.shadowRoot||l)return null;const t=this.getRootNode().querySelectorAll("form");for(const i of Array.from(t))if(i.contains(this))return i;return null}connectedCallback(){var t;super.connectedCallback(),this.containingForm=this.findFormElement(),null===(t=this.containingForm)||void 0===t||t.addEventListener("formdata",this.formDataListener)}disconnectedCallback(){var t;super.disconnectedCallback(),null===(t=this.containingForm)||void 0===t||t.removeEventListener("formdata",this.formDataListener),this.containingForm=null}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(t=>{this.dispatchEvent(new Event("change",t))}))}}p.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,o.__decorate)([(0,s.Cb)({type:Boolean})],p.prototype,"disabled",void 0)},14114:(t,i,e)=>{e.d(i,{P:()=>n});const n=t=>(i,e)=>{if(i.constructor._observers){if(!i.constructor.hasOwnProperty("_observers")){const t=i.constructor._observers;i.constructor._observers=new Map,t.forEach(((t,e)=>i.constructor._observers.set(e,t)))}}else{i.constructor._observers=new Map;const t=i.updated;i.updated=function(i){t.call(this,i),i.forEach(((t,i)=>{const e=this.constructor._observers.get(i);void 0!==e&&e.call(this,this[i],t)}))}}i.constructor._observers.set(e,t)}},54444:(t,i,e)=>{e(48175);var n=e(9672),a=e(87156),o=e(50856);(0,n.k)({_template:o.d`
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
`,is:"paper-tooltip",hostAttributes:{role:"tooltip",tabindex:-1},properties:{for:{type:String,observer:"_findTarget"},manualMode:{type:Boolean,value:!1,observer:"_manualModeChanged"},position:{type:String,value:"bottom"},fitToVisibleBounds:{type:Boolean,value:!1},offset:{type:Number,value:14},marginTop:{type:Number,value:14},animationDelay:{type:Number,value:500,observer:"_delayChange"},animationEntry:{type:String,value:""},animationExit:{type:String,value:""},animationConfig:{type:Object,value:function(){return{entry:[{name:"fade-in-animation",node:this,timing:{delay:0}}],exit:[{name:"fade-out-animation",node:this}]}}},_showing:{type:Boolean,value:!1}},listeners:{webkitAnimationEnd:"_onAnimationEnd"},get target(){var t=(0,a.vz)(this).parentNode,i=(0,a.vz)(this).getOwnerRoot();return this.for?(0,a.vz)(i).querySelector("#"+this.for):t.nodeType==Node.DOCUMENT_FRAGMENT_NODE?i.host:t},attached:function(){this._findTarget()},detached:function(){this.manualMode||this._removeListeners()},playAnimation:function(t){"entry"===t?this.show():"exit"===t&&this.hide()},cancelAnimation:function(){this.$.tooltip.classList.add("cancel-animation")},show:function(){if(!this._showing){if(""===(0,a.vz)(this).textContent.trim()){for(var t=!0,i=(0,a.vz)(this).getEffectiveChildNodes(),e=0;e<i.length;e++)if(""!==i[e].textContent.trim()){t=!1;break}if(t)return}this._showing=!0,this.$.tooltip.classList.remove("hidden"),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.updatePosition(),this._animationPlaying=!0,this.$.tooltip.classList.add(this._getAnimationType("entry"))}},hide:function(){if(this._showing){if(this._animationPlaying)return this._showing=!1,void this._cancelAnimation();this._onAnimationFinish(),this._showing=!1,this._animationPlaying=!0}},updatePosition:function(){if(this._target&&this.offsetParent){var t=this.offset;14!=this.marginTop&&14==this.offset&&(t=this.marginTop);var i,e,n=this.offsetParent.getBoundingClientRect(),a=this._target.getBoundingClientRect(),o=this.getBoundingClientRect(),s=(a.width-o.width)/2,r=(a.height-o.height)/2,l=a.left-n.left,p=a.top-n.top;switch(this.position){case"top":i=l+s,e=p-o.height-t;break;case"bottom":i=l+s,e=p+a.height+t;break;case"left":i=l-o.width-t,e=p+r;break;case"right":i=l+a.width+t,e=p+r}this.fitToVisibleBounds?(n.left+i+o.width>window.innerWidth?(this.style.right="0px",this.style.left="auto"):(this.style.left=Math.max(0,i)+"px",this.style.right="auto"),n.top+e+o.height>window.innerHeight?(this.style.bottom=n.height-p+t+"px",this.style.top="auto"):(this.style.top=Math.max(-n.top,e)+"px",this.style.bottom="auto")):(this.style.left=i+"px",this.style.top=e+"px")}},_addListeners:function(){this._target&&(this.listen(this._target,"mouseenter","show"),this.listen(this._target,"focus","show"),this.listen(this._target,"mouseleave","hide"),this.listen(this._target,"blur","hide"),this.listen(this._target,"tap","hide")),this.listen(this.$.tooltip,"animationend","_onAnimationEnd"),this.listen(this,"mouseenter","hide")},_findTarget:function(){this.manualMode||this._removeListeners(),this._target=this.target,this.manualMode||this._addListeners()},_delayChange:function(t){500!==t&&this.updateStyles({"--paper-tooltip-delay-in":t+"ms"})},_manualModeChanged:function(){this.manualMode?this._removeListeners():this._addListeners()},_cancelAnimation:function(){this.$.tooltip.classList.remove(this._getAnimationType("entry")),this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.add("hidden")},_onAnimationFinish:function(){this._showing&&(this.$.tooltip.classList.remove(this._getAnimationType("entry")),this.$.tooltip.classList.remove("cancel-animation"),this.$.tooltip.classList.add(this._getAnimationType("exit")))},_onAnimationEnd:function(){this._animationPlaying=!1,this._showing||(this.$.tooltip.classList.remove(this._getAnimationType("exit")),this.$.tooltip.classList.add("hidden"))},_getAnimationType:function(t){if("entry"===t&&""!==this.animationEntry)return this.animationEntry;if("exit"===t&&""!==this.animationExit)return this.animationExit;if(this.animationConfig[t]&&"string"==typeof this.animationConfig[t][0].name){if(this.animationConfig[t][0].timing&&this.animationConfig[t][0].timing.delay&&0!==this.animationConfig[t][0].timing.delay){var i=this.animationConfig[t][0].timing.delay;"entry"===t?this.updateStyles({"--paper-tooltip-delay-in":i+"ms"}):"exit"===t&&this.updateStyles({"--paper-tooltip-delay-out":i+"ms"})}return this.animationConfig[t][0].name}},_removeListeners:function(){this._target&&(this.unlisten(this._target,"mouseenter","show"),this.unlisten(this._target,"focus","show"),this.unlisten(this._target,"mouseleave","hide"),this.unlisten(this._target,"blur","hide"),this.unlisten(this._target,"tap","hide")),this.unlisten(this.$.tooltip,"animationend","_onAnimationEnd"),this.unlisten(this,"mouseenter","hide")}})},3239:(t,i,e)=>{function n(t){if(!t||"object"!=typeof t)return t;if("[object Date]"==Object.prototype.toString.call(t))return new Date(t.getTime());if(Array.isArray(t))return t.map(n);var i={};return Object.keys(t).forEach((function(e){i[e]=n(t[e])})),i}e.d(i,{Z:()=>n})},93217:(t,i,e)=>{e.d(i,{Ud:()=>d});const n=Symbol("Comlink.proxy"),a=Symbol("Comlink.endpoint"),o=Symbol("Comlink.releaseProxy"),s=Symbol("Comlink.finalizer"),r=Symbol("Comlink.thrown"),l=t=>"object"==typeof t&&null!==t||"function"==typeof t,p=new Map([["proxy",{canHandle:t=>l(t)&&t[n],serialize(t){const{port1:i,port2:e}=new MessageChannel;return c(t,i),[e,[e]]},deserialize:t=>(t.start(),d(t))}],["throw",{canHandle:t=>l(t)&&r in t,serialize({value:t}){let i;return i=t instanceof Error?{isError:!0,value:{message:t.message,name:t.name,stack:t.stack}}:{isError:!1,value:t},[i,[]]},deserialize(t){if(t.isError)throw Object.assign(new Error(t.value.message),t.value);throw t.value}}]]);function c(t,i=globalThis,e=["*"]){i.addEventListener("message",(function a(o){if(!o||!o.data)return;if(!function(t,i){for(const e of t){if(i===e||"*"===e)return!0;if(e instanceof RegExp&&e.test(i))return!0}return!1}(e,o.origin))return void console.warn(`Invalid origin '${o.origin}' for comlink proxy`);const{id:l,type:p,path:d}=Object.assign({path:[]},o.data),h=(o.data.argumentList||[]).map(w);let u;try{const i=d.slice(0,-1).reduce(((t,i)=>t[i]),t),e=d.reduce(((t,i)=>t[i]),t);switch(p){case"GET":u=e;break;case"SET":i[d.slice(-1)[0]]=w(o.data.value),u=!0;break;case"APPLY":u=e.apply(i,h);break;case"CONSTRUCT":u=function(t){return Object.assign(t,{[n]:!0})}(new e(...h));break;case"ENDPOINT":{const{port1:i,port2:e}=new MessageChannel;c(t,e),u=function(t,i){return _.set(t,i),t}(i,[i])}break;case"RELEASE":u=void 0;break;default:return}}catch(t){u={value:t,[r]:0}}Promise.resolve(u).catch((t=>({value:t,[r]:0}))).then((e=>{const[n,o]=b(e);i.postMessage(Object.assign(Object.assign({},n),{id:l}),o),"RELEASE"===p&&(i.removeEventListener("message",a),m(i),s in t&&"function"==typeof t[s]&&t[s]())})).catch((t=>{const[e,n]=b({value:new TypeError("Unserializable return value"),[r]:0});i.postMessage(Object.assign(Object.assign({},e),{id:l}),n)}))})),i.start&&i.start()}function m(t){(function(t){return"MessagePort"===t.constructor.name})(t)&&t.close()}function d(t,i){return g(t,[],i)}function h(t){if(t)throw new Error("Proxy has been released and is not useable")}function u(t){return E(t,{type:"RELEASE"}).then((()=>{m(t)}))}const f=new WeakMap,y="FinalizationRegistry"in globalThis&&new FinalizationRegistry((t=>{const i=(f.get(t)||0)-1;f.set(t,i),0===i&&u(t)}));function g(t,i=[],e=function(){}){let n=!1;const s=new Proxy(e,{get(e,a){if(h(n),a===o)return()=>{!function(t){y&&y.unregister(t)}(s),u(t),n=!0};if("then"===a){if(0===i.length)return{then:()=>s};const e=E(t,{type:"GET",path:i.map((t=>t.toString()))}).then(w);return e.then.bind(e)}return g(t,[...i,a])},set(e,a,o){h(n);const[s,r]=b(o);return E(t,{type:"SET",path:[...i,a].map((t=>t.toString())),value:s},r).then(w)},apply(e,o,s){h(n);const r=i[i.length-1];if(r===a)return E(t,{type:"ENDPOINT"}).then(w);if("bind"===r)return g(t,i.slice(0,-1));const[l,p]=v(s);return E(t,{type:"APPLY",path:i.map((t=>t.toString())),argumentList:l},p).then(w)},construct(e,a){h(n);const[o,s]=v(a);return E(t,{type:"CONSTRUCT",path:i.map((t=>t.toString())),argumentList:o},s).then(w)}});return function(t,i){const e=(f.get(i)||0)+1;f.set(i,e),y&&y.register(t,i,t)}(s,t),s}function v(t){const i=t.map(b);return[i.map((t=>t[0])),(e=i.map((t=>t[1])),Array.prototype.concat.apply([],e))];var e}const _=new WeakMap;function b(t){for(const[i,e]of p)if(e.canHandle(t)){const[n,a]=e.serialize(t);return[{type:"HANDLER",name:i,value:n},a]}return[{type:"RAW",value:t},_.get(t)||[]]}function w(t){switch(t.type){case"HANDLER":return p.get(t.name).deserialize(t.value);case"RAW":return t.value}}function E(t,i,e){return new Promise((n=>{const a=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");t.addEventListener("message",(function i(e){e.data&&e.data.id&&e.data.id===a&&(t.removeEventListener("message",i),n(e.data))})),t.start&&t.start(),t.postMessage(Object.assign({id:a},i),e)}))}},81563:(t,i,e)=>{e.d(i,{E_:()=>y,OR:()=>l,_Y:()=>c,dZ:()=>r,fk:()=>m,hN:()=>s,hl:()=>h,i9:()=>u,pt:()=>o,ws:()=>f});var n=e(15304);const{I:a}=n._$LH,o=t=>null===t||"object"!=typeof t&&"function"!=typeof t,s=(t,i)=>void 0===i?void 0!==(null==t?void 0:t._$litType$):(null==t?void 0:t._$litType$)===i,r=t=>{var i;return null!=(null===(i=null==t?void 0:t._$litType$)||void 0===i?void 0:i.h)},l=t=>void 0===t.strings,p=()=>document.createComment(""),c=(t,i,e)=>{var n;const o=t._$AA.parentNode,s=void 0===i?t._$AB:i._$AA;if(void 0===e){const i=o.insertBefore(p(),s),n=o.insertBefore(p(),s);e=new a(i,n,t,t.options)}else{const i=e._$AB.nextSibling,a=e._$AM,r=a!==t;if(r){let i;null===(n=e._$AQ)||void 0===n||n.call(e,t),e._$AM=t,void 0!==e._$AP&&(i=t._$AU)!==a._$AU&&e._$AP(i)}if(i!==s||r){let t=e._$AA;for(;t!==i;){const i=t.nextSibling;o.insertBefore(t,s),t=i}}}return e},m=(t,i,e=t)=>(t._$AI(i,e),t),d={},h=(t,i=d)=>t._$AH=i,u=t=>t._$AH,f=t=>{var i;null===(i=t._$AP)||void 0===i||i.call(t,!1,!0);let e=t._$AA;const n=t._$AB.nextSibling;for(;e!==n;){const t=e.nextSibling;e.remove(),e=t}},y=t=>{t._$AR()}},57835:(t,i,e)=>{e.d(i,{XM:()=>n.XM,Xe:()=>n.Xe,pX:()=>n.pX});var n=e(38941)}}]);
//# sourceMappingURL=94dd532b.js.map