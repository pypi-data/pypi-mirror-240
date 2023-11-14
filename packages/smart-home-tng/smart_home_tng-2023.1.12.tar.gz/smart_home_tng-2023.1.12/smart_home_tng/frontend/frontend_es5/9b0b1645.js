"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[3143],{56949:function(t,e,r){r.d(e,{q:function(){return i}});var a=r(56007);const i=t=>{if(a.V_.includes(t.state))return t.state;const e=t.entity_id.split(".")[0];let r=t.state;return"climate"===e&&(r=t.attributes.hvac_action),r}},52797:function(t,e,r){r.d(e,{N:function(){return a}});const a=r(37500).iv`
  ha-state-icon[data-domain="alert"][data-state="on"],
  ha-state-icon[data-domain="automation"][data-state="on"],
  ha-state-icon[data-domain="binary_sensor"][data-state="on"],
  ha-state-icon[data-domain="calendar"][data-state="on"],
  ha-state-icon[data-domain="camera"][data-state="streaming"],
  ha-state-icon[data-domain="cover"][data-state="open"],
  ha-state-icon[data-domain="device_tracker"][data-state="home"],
  ha-state-icon[data-domain="fan"][data-state="on"],
  ha-state-icon[data-domain="humidifier"][data-state="on"],
  ha-state-icon[data-domain="light"][data-state="on"],
  ha-state-icon[data-domain="input_boolean"][data-state="on"],
  ha-state-icon[data-domain="lock"][data-state="unlocked"],
  ha-state-icon[data-domain="media_player"][data-state="on"],
  ha-state-icon[data-domain="media_player"][data-state="paused"],
  ha-state-icon[data-domain="media_player"][data-state="playing"],
  ha-state-icon[data-domain="remote"][data-state="on"],
  ha-state-icon[data-domain="script"][data-state="on"],
  ha-state-icon[data-domain="sun"][data-state="above_horizon"],
  ha-state-icon[data-domain="switch"][data-state="on"],
  ha-state-icon[data-domain="timer"][data-state="active"],
  ha-state-icon[data-domain="vacuum"][data-state="cleaning"],
  ha-state-icon[data-domain="group"][data-state="on"],
  ha-state-icon[data-domain="group"][data-state="home"],
  ha-state-icon[data-domain="group"][data-state="open"],
  ha-state-icon[data-domain="group"][data-state="locked"],
  ha-state-icon[data-domain="group"][data-state="problem"] {
    color: var(--paper-item-icon-active-color, #fdd835);
  }

  ha-state-icon[data-domain="climate"][data-state="cooling"] {
    color: var(--cool-color, var(--state-climate-cool-color));
  }

  ha-state-icon[data-domain="climate"][data-state="heating"] {
    color: var(--heat-color, var(--state-climate-heat-color));
  }

  ha-state-icon[data-domain="climate"][data-state="drying"] {
    color: var(--dry-color, var(--state-climate-dry-color));
  }

  ha-state-icon[data-domain="alarm_control_panel"] {
    color: var(--alarm-color-armed, var(--label-badge-red));
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="disarmed"] {
    color: var(--alarm-color-disarmed, var(--label-badge-green));
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="pending"],
  ha-state-icon[data-domain="alarm_control_panel"][data-state="arming"] {
    color: var(--alarm-color-pending, var(--label-badge-yellow));
    animation: pulse 1s infinite;
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="triggered"] {
    color: var(--alarm-color-triggered, var(--label-badge-red));
    animation: pulse 1s infinite;
  }

  @keyframes pulse {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  ha-state-icon[data-domain="plant"][data-state="problem"] {
    color: var(--state-icon-error-color);
  }

  /* Color the icon if unavailable */
  ha-state-icon[data-state="unavailable"] {
    color: var(--state-unavailable-color);
  }
`},43426:function(t,e,r){r.d(e,{U:function(){return a}});const a=async(t,e,r,a,i,...n)=>{let o=a[t];o||(o=a[t]={});const s=o[i];if(s)return s;const c=r(a,i,...n);return o[i]=c,c.then((()=>setTimeout((()=>{o[i]=void 0}),e)),(()=>{o[i]=void 0})),c}},3143:function(t,e,r){var a=r(37500),i=r(36924),n=r(51346),o=r(70483),s=r(56949),c=r(58831),l=r(22311),d=r(52797),u=r(89439);r(99724);function f(){f=function(){return t};var t={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(t,e){["method","field"].forEach((function(r){e.forEach((function(e){e.kind===r&&"own"===e.placement&&this.defineClassElement(t,e)}),this)}),this)},initializeClassElements:function(t,e){var r=t.prototype;["method","field"].forEach((function(a){e.forEach((function(e){var i=e.placement;if(e.kind===a&&("static"===i||"prototype"===i)){var n="static"===i?t:r;this.defineClassElement(n,e)}}),this)}),this)},defineClassElement:function(t,e){var r=e.descriptor;if("field"===e.kind){var a=e.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===a?void 0:a.call(t)}}Object.defineProperty(t,e.key,r)},decorateClass:function(t,e){var r=[],a=[],i={static:[],prototype:[],own:[]};if(t.forEach((function(t){this.addElementPlacement(t,i)}),this),t.forEach((function(t){if(!m(t))return r.push(t);var e=this.decorateElement(t,i);r.push(e.element),r.push.apply(r,e.extras),a.push.apply(a,e.finishers)}),this),!e)return{elements:r,finishers:a};var n=this.decorateConstructor(r,e);return a.push.apply(a,n.finishers),n.finishers=a,n},addElementPlacement:function(t,e,r){var a=e[t.placement];if(!r&&-1!==a.indexOf(t.key))throw new TypeError("Duplicated element ("+t.key+")");a.push(t.key)},decorateElement:function(t,e){for(var r=[],a=[],i=t.decorators,n=i.length-1;n>=0;n--){var o=e[t.placement];o.splice(o.indexOf(t.key),1);var s=this.fromElementDescriptor(t),c=this.toElementFinisherExtras((0,i[n])(s)||s);t=c.element,this.addElementPlacement(t,e),c.finisher&&a.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],e);r.push.apply(r,l)}}return{element:t,finishers:a,extras:r}},decorateConstructor:function(t,e){for(var r=[],a=e.length-1;a>=0;a--){var i=this.fromClassDescriptor(t),n=this.toClassDescriptor((0,e[a])(i)||i);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){t=n.elements;for(var o=0;o<t.length-1;o++)for(var s=o+1;s<t.length;s++)if(t[o].key===t[s].key&&t[o].placement===t[s].placement)throw new TypeError("Duplicated element ("+t[o].key+")")}}return{elements:t,finishers:r}},fromElementDescriptor:function(t){var e={kind:t.kind,key:t.key,placement:t.placement,descriptor:t.descriptor};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===t.kind&&(e.initializer=t.initializer),e},toElementDescriptors:function(t){var e;if(void 0!==t)return(e=t,function(t){if(Array.isArray(t))return t}(e)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(e)||function(t,e){if(t){if("string"==typeof t)return g(t,e);var r=Object.prototype.toString.call(t).slice(8,-1);return"Object"===r&&t.constructor&&(r=t.constructor.name),"Map"===r||"Set"===r?Array.from(t):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?g(t,e):void 0}}(e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(t){var e=this.toElementDescriptor(t);return this.disallowProperty(t,"finisher","An element descriptor"),this.disallowProperty(t,"extras","An element descriptor"),e}),this)},toElementDescriptor:function(t){var e=String(t.kind);if("method"!==e&&"field"!==e)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+e+'"');var r=b(t.key),a=String(t.placement);if("static"!==a&&"prototype"!==a&&"own"!==a)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+a+'"');var i=t.descriptor;this.disallowProperty(t,"elements","An element descriptor");var n={kind:e,key:r,placement:a,descriptor:Object.assign({},i)};return"field"!==e?this.disallowProperty(t,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),n.initializer=t.initializer),n},toElementFinisherExtras:function(t){return{element:this.toElementDescriptor(t),finisher:y(t,"finisher"),extras:this.toElementDescriptors(t.extras)}},fromClassDescriptor:function(t){var e={kind:"class",elements:t.map(this.fromElementDescriptor,this)};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),e},toClassDescriptor:function(t){var e=String(t.kind);if("class"!==e)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+e+'"');this.disallowProperty(t,"key","A class descriptor"),this.disallowProperty(t,"placement","A class descriptor"),this.disallowProperty(t,"descriptor","A class descriptor"),this.disallowProperty(t,"initializer","A class descriptor"),this.disallowProperty(t,"extras","A class descriptor");var r=y(t,"finisher");return{elements:this.toElementDescriptors(t.elements),finisher:r}},runClassFinishers:function(t,e){for(var r=0;r<e.length;r++){var a=(0,e[r])(t);if(void 0!==a){if("function"!=typeof a)throw new TypeError("Finishers must return a constructor.");t=a}}return t},disallowProperty:function(t,e,r){if(void 0!==t[e])throw new TypeError(r+" can't have a ."+e+" property.")}};return t}function h(t){var e,r=b(t.key);"method"===t.kind?e={value:t.value,writable:!0,configurable:!0,enumerable:!1}:"get"===t.kind?e={get:t.value,configurable:!0,enumerable:!1}:"set"===t.kind?e={set:t.value,configurable:!0,enumerable:!1}:"field"===t.kind&&(e={configurable:!0,writable:!0,enumerable:!0});var a={kind:"field"===t.kind?"field":"method",key:r,placement:t.static?"static":"field"===t.kind?"own":"prototype",descriptor:e};return t.decorators&&(a.decorators=t.decorators),"field"===t.kind&&(a.initializer=t.value),a}function p(t,e){void 0!==t.descriptor.get?e.descriptor.get=t.descriptor.get:e.descriptor.set=t.descriptor.set}function m(t){return t.decorators&&t.decorators.length}function v(t){return void 0!==t&&!(void 0===t.value&&void 0===t.writable)}function y(t,e){var r=t[e];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+e+"' to be a function");return r}function b(t){var e=function(t,e){if("object"!=typeof t||null===t)return t;var r=t[Symbol.toPrimitive];if(void 0!==r){var a=r.call(t,e||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===e?String:Number)(t)}(t,"string");return"symbol"==typeof e?e:String(e)}function g(t,e){(null==e||e>t.length)&&(e=t.length);for(var r=0,a=new Array(e);r<e;r++)a[r]=t[r];return a}function k(){return k="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(t,e,r){var a=function(t,e){for(;!Object.prototype.hasOwnProperty.call(t,e)&&null!==(t=w(t)););return t}(t,e);if(a){var i=Object.getOwnPropertyDescriptor(a,e);return i.get?i.get.call(arguments.length<3?t:r):i.value}},k.apply(this,arguments)}function w(t){return w=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},w(t)}let _=function(t,e,r,a){var i=f();if(a)for(var n=0;n<a.length;n++)i=a[n](i);var o=e((function(t){i.initializeInstanceElements(t,s.elements)}),r),s=i.decorateClass(function(t){for(var e=[],r=function(t){return"method"===t.kind&&t.key===n.key&&t.placement===n.placement},a=0;a<t.length;a++){var i,n=t[a];if("method"===n.kind&&(i=e.find(r)))if(v(n.descriptor)||v(i.descriptor)){if(m(n)||m(i))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");i.descriptor=n.descriptor}else{if(m(n)){if(m(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");i.decorators=n.decorators}p(n,i)}else e.push(n)}return e}(o.d.map(h)),t);return i.initializeClassElements(o.F,s.elements),i.runClassFinishers(o.F,s.finishers)}(null,(function(t,e){class r extends e{constructor(...e){super(...e),t(this)}}return{F:r,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"stateObj",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"overrideIcon",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"overrideImage",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"stateColor",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,reflect:!0,attribute:"icon"})],key:"_showIcon",value(){return!0}},{kind:"field",decorators:[(0,i.SB)()],key:"_iconStyle",value(){return{}}},{kind:"method",key:"render",value:function(){const t=this.stateObj;if(!t&&!this.overrideIcon&&!this.overrideImage)return a.dy`<div class="missing">
        <ha-svg-icon .path=${"M13 14H11V9H13M13 18H11V16H13M1 21H23L12 2L1 21Z"}></ha-svg-icon>
      </div>`;if(!this._showIcon)return a.dy``;const e=t?(0,l.N)(t):void 0;return a.dy`<ha-state-icon
      style=${(0,o.V)(this._iconStyle)}
      data-domain=${(0,n.o)(this.stateColor||"light"===e&&!1!==this.stateColor?e:void 0)}
      data-state=${t?(0,s.q)(t):""}
      .icon=${this.overrideIcon}
      .state=${t}
    ></ha-state-icon>`}},{kind:"method",key:"willUpdate",value:function(t){if(k(w(r.prototype),"willUpdate",this).call(this,t),!t.has("stateObj")&&!t.has("overrideImage")&&!t.has("overrideIcon"))return;const e=this.stateObj,a={},i={backgroundImage:""};if(this._showIcon=!0,e&&void 0===this.overrideImage)if(!e.attributes.entity_picture_local&&!e.attributes.entity_picture||this.overrideIcon){if("on"===e.state&&(!1!==this.stateColor&&e.attributes.rgb_color&&(a.color=`rgb(${e.attributes.rgb_color.join(",")})`),e.attributes.brightness&&!1!==this.stateColor)){const t=e.attributes.brightness;if("number"!=typeof t){const r=`Type error: state-badge expected number, but type of ${e.entity_id}.attributes.brightness is ${typeof t} (${t})`;console.warn(r)}a.filter=`brightness(${(t+245)/5}%)`}}else{let t=e.attributes.entity_picture_local||e.attributes.entity_picture;this.hass&&(t=this.hass.hassUrl(t)),"camera"===(0,c.M)(e.entity_id)&&(t=(0,u.Ch)(t,80,80)),i.backgroundImage=`url(${t})`,this._showIcon=!1}else if(this.overrideImage){let t=this.overrideImage;this.hass&&(t=this.hass.hassUrl(t)),i.backgroundImage=`url(${t})`,this._showIcon=!1}this._iconStyle=a,Object.assign(this.style,i)}},{kind:"get",static:!0,key:"styles",value:function(){return[d.N,a.iv`
        :host {
          position: relative;
          display: inline-block;
          width: 40px;
          color: var(--paper-item-icon-color, #44739e);
          border-radius: 50%;
          height: 40px;
          text-align: center;
          background-size: cover;
          line-height: 40px;
          vertical-align: middle;
          box-sizing: border-box;
        }
        :host(:focus) {
          outline: none;
        }
        :host(:not([icon]):focus) {
          border: 2px solid var(--divider-color);
        }
        :host([icon]:focus) {
          background: var(--divider-color);
        }
        ha-state-icon {
          transition: color 0.3s ease-in-out, filter 0.3s ease-in-out;
        }
        .missing {
          color: #fce588;
        }
      `]}}]}}),a.oi);customElements.define("state-badge",_)},89439:function(t,e,r){if(r.d(e,{B:function(){return y},Ch:function(){return c},Lr:function(){return f},Mw:function(){return m},Xn:function(){return p},i4:function(){return d},jU:function(){return s},kU:function(){return o},nk:function(){return l},qW:function(){return n},tb:function(){return h},zj:function(){return b}}),98818!=r.j)var a=r(43426);if(98818!=r.j)var i=r(22814);const n=2,o="hls",s="web_rtc",c=(t,e,r)=>`${t}&width=${e}&height=${r}`,l=t=>`/api/camera_proxy_stream/${t.entity_id}?token=${t.attributes.access_token}`,d=async(t,e,r,i)=>{const n=await(0,a.U)("_cameraTmbUrl",9e3,u,t,e);return c(n,r,i)},u=async(t,e)=>{const r=await(0,i.iI)(t,`/api/camera_proxy/${e}`);return t.hassUrl(r.path)},f=async(t,e,r)=>{const a={type:"camera/stream",entity_id:e};r&&(a.format=r);const i=await t.callWS(a);return i.url=t.hassUrl(i.url),i},h=(t,e,r)=>t.callWS({type:"camera/web_rtc_offer",entity_id:e,offer:r}),p=(t,e)=>t.callWS({type:"camera/get_prefs",entity_id:e}),m=(t,e,r)=>t.callWS(Object.assign({type:"camera/update_prefs",entity_id:e},r)),v="media-source://camera/",y=t=>t.startsWith(v),b=t=>t.substring(22)},56007:function(t,e,r){r.d(e,{V_:function(){return n},lz:function(){return i},nZ:function(){return a}});const a="unavailable",i="unknown",n=[a,i]}}]);
//# sourceMappingURL=9b0b1645.js.map