/*! For license information please see 65f604a4.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[88369],{89194:(e,t,r)=>{r(48175),r(65660),r(70019);var i=r(9672),n=r(50856);(0,i.k)({_template:n.d`
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
`,is:"paper-item-body"})},55158:(e,t,r)=>{r.r(t),r.d(t,{EnergySetupWizard:()=>v});var i=r(37500),n=r(33310),s=r(47181),o=r(55424),a=(r(51187),r(99012),r(84744),r(74982),r(2447),r(74501),r(11654)),l=r(26765);function c(){c=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var s="static"===n?e:r;this.defineClassElement(s,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!h(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var s=this.decorateConstructor(r,t);return i.push.apply(i,s.finishers),s.finishers=i,s},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,s=n.length-1;s>=0;s--){var o=t[e.placement];o.splice(o.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[s])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),s=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==s.finisher&&r.push(s.finisher),void 0!==s.elements){e=s.elements;for(var o=0;o<e.length-1;o++)for(var a=o+1;a<e.length;a++)if(e[o].key===e[a].key&&e[o].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[o].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return m(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?m(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=y(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var s={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),s.initializer=e.initializer),s},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:u(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=u(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function d(e){var t,r=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function h(e){return e.decorators&&e.decorators.length}function f(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function u(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}let v=function(e,t,r,i){var n=c();if(i)for(var s=0;s<i.length;s++)n=i[s](n);var o=t((function(e){n.initializeInstanceElements(e,a.elements)}),r),a=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===s.key&&e.placement===s.placement},i=0;i<e.length;i++){var n,s=e[i];if("method"===s.kind&&(n=t.find(r)))if(f(s.descriptor)||f(n.descriptor)){if(h(s)||h(n))throw new ReferenceError("Duplicated methods ("+s.key+") can't be decorated.");n.descriptor=s.descriptor}else{if(h(s)){if(h(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+s.key+").");n.decorators=s.decorators}p(s,n)}else t.push(s)}return t}(o.d.map(d)),e);return n.initializeClassElements(o.F,a.elements),n.runClassFinishers(o.F,a.finishers)}([(0,n.Mo)("energy-setup-wizard-card")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"lovelace",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_info",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_step",value:()=>0},{kind:"field",decorators:[(0,n.SB)()],key:"_preferences",value:()=>({energy_sources:[],device_consumption:[]})},{kind:"method",key:"getCardSize",value:function(){return 10}},{kind:"method",key:"setConfig",value:function(e){e.preferences&&(this._preferences=e.preferences)}},{kind:"method",key:"firstUpdated",value:function(){this.hass.loadFragmentTranslation("config"),this._fetchconfig()}},{kind:"method",key:"render",value:function(){return i.dy`
      <p>
        ${this.hass.localize("ui.panel.energy.setup.step",{step:this._step+1,steps:5})}
      </p>
      ${0===this._step?i.dy`<ha-energy-grid-settings
            .hass=${this.hass}
            .preferences=${this._preferences}
            @value-changed=${this._prefsChanged}
          ></ha-energy-grid-settings>`:1===this._step?i.dy`<ha-energy-solar-settings
            .hass=${this.hass}
            .preferences=${this._preferences}
            .info=${this._info}
            @value-changed=${this._prefsChanged}
          ></ha-energy-solar-settings>`:2===this._step?i.dy`<ha-energy-battery-settings
            .hass=${this.hass}
            .preferences=${this._preferences}
            @value-changed=${this._prefsChanged}
          ></ha-energy-battery-settings>`:3===this._step?i.dy`<ha-energy-gas-settings
            .hass=${this.hass}
            .preferences=${this._preferences}
            @value-changed=${this._prefsChanged}
          ></ha-energy-gas-settings>`:i.dy`<ha-energy-device-settings
            .hass=${this.hass}
            .preferences=${this._preferences}
            @value-changed=${this._prefsChanged}
          ></ha-energy-device-settings>`}
      <div class="buttons">
        ${this._step>0?i.dy`<mwc-button outlined @click=${this._back}
              >${this.hass.localize("ui.panel.energy.setup.back")}</mwc-button
            >`:i.dy`<div></div>`}
        ${this._step<4?i.dy`<mwc-button unelevated @click=${this._next}
              >${this.hass.localize("ui.panel.energy.setup.next")}</mwc-button
            >`:i.dy`<mwc-button unelevated @click=${this._setupDone}>
              ${this.hass.localize("ui.panel.energy.setup.done")}
            </mwc-button>`}
      </div>
    `}},{kind:"method",key:"_fetchconfig",value:async function(){this._info=await(0,o.xZ)(this.hass)}},{kind:"method",key:"_prefsChanged",value:function(e){this._preferences=e.detail.value}},{kind:"method",key:"_back",value:function(){0!==this._step&&this._step--}},{kind:"method",key:"_next",value:function(){4!==this._step&&this._step++}},{kind:"method",key:"_setupDone",value:async function(){if(this._preferences){try{this._preferences=await(0,o._Z)(this.hass,this._preferences)}catch(e){(0,l.Ys)(this,{title:`Failed to save config: ${e.message}`})}(0,s.B)(this,"reload-energy-panel")}}},{kind:"get",static:!0,key:"styles",value:function(){return[a.Qx,i.iv`
        :host {
          display: block;
          padding: 16px;
          max-width: 700px;
          margin: 0 auto;
        }
        mwc-button {
          margin-top: 8px;
        }
        .buttons {
          display: flex;
          justify-content: space-between;
        }
      `]}}]}}),i.oi)}}]);
//# sourceMappingURL=65f604a4.js.map