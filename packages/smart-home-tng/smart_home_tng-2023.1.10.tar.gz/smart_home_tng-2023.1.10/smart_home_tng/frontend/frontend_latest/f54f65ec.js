"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[66621],{66621:(e,t,i)=>{i.a(e,(async(e,r)=>{try{i.r(t);var n=i(37500),o=i(36924),s=i(8636),a=i(51346),c=i(49706),l=i(62877),d=i(58831),h=i(29171),f=i(91741),u=(i(22098),i(10983),i(99724),i(93491)),p=i(15688),m=i(22503),g=i(22193),y=i(53658),v=i(90271),b=(i(97282),i(75502)),w=(i(65082),e([h]));function k(e,t,i,r){var n=_();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass($(s.d.map(E)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function _(){_=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!D(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,n[o])(a)||a);e=c.element,this.addElementPlacement(e,t),c.finisher&&r.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);i.push.apply(i,l)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,F(t)||j(t)||O(t)||z()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=A(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:C(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=C(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function E(e){var t,i=A(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function x(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function $(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(P(o.descriptor)||P(n.descriptor)){if(D(o)||D(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(D(o)){if(D(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}x(o,n)}else t.push(o)}return t}function D(e){return e.decorators&&e.decorators.length}function P(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function C(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function A(e){var t=T(e,"string");return"symbol"==typeof t?t:String(t)}function T(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function z(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function O(e,t){if(e){if("string"==typeof e)return S(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?S(e,t):void 0}}function S(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function j(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function F(e){if(Array.isArray(e))return e}function I(){return I="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=R(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},I.apply(this,arguments)}function R(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=H(e)););return e}function H(e){return H=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},H(e)}h=(w.then?(await w)():w)[0];const K=new Set(["closed","locked","not_home","off"]);k([(0,o.Mo)("hui-picture-glance-card")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"method",static:!0,key:"getConfigElement",value:async function(){return await Promise.all([i.e(29563),i.e(98985),i.e(24103),i.e(23355),i.e(2462),i.e(41985),i.e(45507),i.e(51882),i.e(77426),i.e(63519),i.e(2216),i.e(12545),i.e(13701),i.e(77576),i.e(74535),i.e(46583),i.e(53822),i.e(23956),i.e(68101),i.e(67622),i.e(14005),i.e(93796),i.e(63681),i.e(48456),i.e(61788),i.e(41759),i.e(85316),i.e(33785)]).then(i.bind(i,33785)),document.createElement("hui-picture-glance-card-editor")}},{kind:"method",static:!0,key:"getStubConfig",value:function(e,t,i){return{type:"picture-glance",title:"Kitchen",image:"https://demo.home-assistant.io/stub_config/kitchen.png",entities:(0,p.j)(e,2,t,i,["sensor","binary_sensor"])}}},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_config",value:void 0},{kind:"field",key:"_entitiesDialog",value:void 0},{kind:"field",key:"_entitiesToggle",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(e){if(!e||!e.entities||!Array.isArray(e.entities)||!(e.image||e.camera_image||e.state_image)||e.state_image&&!e.entity)throw new Error("Invalid configuration");const t=(0,v.A)(e.entities);this._entitiesDialog=[],this._entitiesToggle=[],t.forEach((t=>{e.force_dialog||!c.Kk.has((0,d.M)(t.entity))?this._entitiesDialog.push(t):this._entitiesToggle.push(t)})),this._config={hold_action:{action:"more-info"},...e}}},{kind:"method",key:"shouldUpdate",value:function(e){if((0,y.G)(this,e))return!0;const t=e.get("hass");if(!t||t.themes!==this.hass.themes||t.locale!==this.hass.locale)return!0;if(this._entitiesDialog)for(const e of this._entitiesDialog)if(t.states[e.entity]!==this.hass.states[e.entity])return!0;if(this._entitiesToggle)for(const e of this._entitiesToggle)if(t.states[e.entity]!==this.hass.states[e.entity])return!0;return!1}},{kind:"method",key:"updated",value:function(e){if(I(H(r.prototype),"updated",this).call(this,e),!this._config||!this.hass)return;const t=e.get("hass"),i=e.get("_config");t&&i&&t.themes===this.hass.themes&&i.theme===this._config.theme||(0,l.R)(this,this.hass.themes,this._config.theme)}},{kind:"method",key:"render",value:function(){return this._config&&this.hass?n.dy`
      <ha-card>
        <hui-image
          class=${(0,s.$)({clickable:Boolean(this._config.tap_action||this._config.hold_action||this._config.camera_image)})}
          @action=${this._handleAction}
          .actionHandler=${(0,u.K)({hasHold:(0,g._)(this._config.hold_action),hasDoubleClick:(0,g._)(this._config.double_tap_action)})}
          tabindex=${(0,a.o)((0,g._)(this._config.tap_action)?"0":void 0)}
          .config=${this._config}
          .hass=${this.hass}
          .image=${this._config.image}
          .stateImage=${this._config.state_image}
          .stateFilter=${this._config.state_filter}
          .cameraImage=${this._config.camera_image}
          .cameraView=${this._config.camera_view}
          .entity=${this._config.entity}
          .aspectRatio=${this._config.aspect_ratio}
        ></hui-image>
        <div class="box">
          ${this._config.title?n.dy` <div class="title">${this._config.title}</div> `:""}
          <div class="row">
            ${this._entitiesDialog.map((e=>this.renderEntity(e,!0)))}
          </div>
          <div class="row">
            ${this._entitiesToggle.map((e=>this.renderEntity(e,!1)))}
          </div>
        </div>
      </ha-card>
    `:n.dy``}},{kind:"method",key:"renderEntity",value:function(e,t){const i=this.hass.states[e.entity];return e={tap_action:{action:t?"more-info":"toggle"},hold_action:{action:"more-info"},...e},i?n.dy`
      <div class="wrapper">
        <ha-icon-button
          @action=${this._handleAction}
          .actionHandler=${(0,u.K)({hasHold:(0,g._)(e.hold_action),hasDoubleClick:(0,g._)(e.double_tap_action)})}
          tabindex=${(0,a.o)((0,g._)(e.tap_action)?void 0:"-1")}
          .disabled=${!(0,g._)(e.tap_action)}
          .config=${e}
          class=${(0,s.$)({"state-on":!K.has(i.state)})}
          title=${`${(0,f.C)(i)} : ${(0,h.D)(this.hass.localize,i,this.hass.locale)}`}
        >
          <ha-state-icon
            .icon=${e.icon}
            .state=${i}
          ></ha-state-icon>
        </ha-icon-button>

        ${!0!==this._config.show_state&&!0!==e.show_state?n.dy`<div class="state"></div>`:n.dy`
              <div class="state">
                ${e.attribute?n.dy`
                      ${e.prefix}${i.attributes[e.attribute]}${e.suffix}
                    `:(0,h.D)(this.hass.localize,i,this.hass.locale)}
              </div>
            `}
      </div>
    `:n.dy`
        <hui-warning-element
          .label=${(0,b.i)(this.hass,e.entity)}
        ></hui-warning-element>
      `}},{kind:"method",key:"_handleAction",value:function(e){const t=e.currentTarget.config;(0,m.G)(this,this.hass,t,e.detail.action)}},{kind:"get",static:!0,key:"styles",value:function(){return n.iv`
      ha-card {
        position: relative;
        min-height: 48px;
        overflow: hidden;
        height: 100%;
        box-sizing: border-box;
      }

      hui-image.clickable {
        cursor: pointer;
      }

      .box {
        /* start paper-font-common-nowrap style */
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        /* end paper-font-common-nowrap style */

        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: var(
          --ha-picture-card-background-color,
          rgba(0, 0, 0, 0.3)
        );
        padding: 4px 8px;
        font-size: 16px;
        line-height: 40px;
        color: var(--ha-picture-card-text-color, white);
        display: flex;
        justify-content: space-between;
        flex-direction: row;
      }

      .box .title {
        font-weight: 500;
        margin-left: 8px;
      }

      ha-icon-button {
        --mdc-icon-button-size: 40px;
        --disabled-text-color: currentColor;
        color: var(--ha-picture-icon-button-color, #a9a9a9);
      }

      ha-icon-button.state-on {
        color: var(--ha-picture-icon-button-on-color, white);
      }
      hui-warning-element {
        padding: 0 8px;
      }
      .state {
        display: block;
        font-size: 12px;
        text-align: center;
        line-height: 12px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .row {
        display: flex;
        flex-direction: row;
      }
      .wrapper {
        display: flex;
        flex-direction: column;
        width: 40px;
      }
    `}}]}}),n.oi);r()}catch(M){r(M)}}))}}]);
//# sourceMappingURL=f54f65ec.js.map