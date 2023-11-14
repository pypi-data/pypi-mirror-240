"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[36898],{5435:function(e,t,i){i.d(t,{G:function(){return n}});var r=i(14516);i(92874);const o=(0,r.Z)((e=>new Intl.RelativeTimeFormat(e.language,{numeric:"auto"}))),n=(e,t,i,r=!0)=>{const n=function(e,t,i){void 0===t&&(t=new Date);void 0===i&&(i=u);var r=(+e-+t)/a;if(Math.abs(r)<i.second)return{value:Math.round(r),unit:"second"};var o=r/s;if(Math.abs(o)<i.minute)return{value:Math.round(o),unit:"minute"};var n=r/l;if(Math.abs(n)<i.hour)return{value:Math.round(n),unit:"hour"};var h=r/c;if(Math.abs(h)<i.day)return{value:Math.round(h),unit:"day"};var p=new Date(e),f=new Date(t),m=p.getFullYear()-f.getFullYear();if(Math.round(Math.abs(m))>0)return{value:Math.round(m),unit:"year"};var y=12*m+p.getMonth()-f.getMonth();if(Math.round(Math.abs(y))>0)return{value:Math.round(y),unit:"month"};var v=r/d;return{value:Math.round(v),unit:"week"}}(e,i);return r?o(t).format(n.value,n.unit):Intl.NumberFormat(t.language,{style:"unit",unit:n.unit,unitDisplay:"long"}).format(Math.abs(n.value))},a=1e3,s=60,l=60*s,c=24*l,d=7*c;const u={second:45,minute:45,hour:22,day:5}},36898:function(e,t,i){i.r(t);var r=i(36924),o=i(14516),n=i(22311),a=i(38346),s=i(18199),l=(i(51187),i(44577),i(53268),i(12730),i(37500)),c=i(8636),d=i(47181),u=i(83849),h=i(50577),p=(i(81545),i(22098),i(36125),i(10983),i(52039),i(18900),i(93748)),f=i(26765),m=(i(27849),i(60010),i(23670)),y=i(11654),v=i(81796);i(88165);const g=()=>Promise.all([i.e(85084),i.e(75049)]).then(i.bind(i,75049)),b=()=>Promise.all([i.e(85084),i.e(74365)]).then(i.bind(i,74365));i(13266),i(31206),i(4940),i(97383),i(14089),i(3555),i(9381);var k=i(86490);function w(){w=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var o=t.placement;if(t.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!A(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return z(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?z(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=P(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:$(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=$(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function _(e){var t,i=P(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function E(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function A(e){return e.decorators&&e.decorators.length}function C(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function $(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function P(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function z(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function x(){return x="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=O(e)););return e}(e,t);if(r){var o=Object.getOwnPropertyDescriptor(r,t);return o.get?o.get.call(arguments.length<3?e:i):o.value}},x.apply(this,arguments)}function O(e){return O=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},O(e)}!function(e,t,i,r){var o=w();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),i),s=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var o,n=e[r];if("method"===n.kind&&(o=t.find(i)))if(C(n.descriptor)||C(o.descriptor)){if(A(n)||A(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(A(n)){if(A(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}E(n,o)}else t.push(n)}return t}(a.d.map(_)),e);o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,r.Mo)("blueprint-automation-editor")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,r.Cb)({reflect:!0,type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"config",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"stateObj",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_blueprints",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){x(O(i.prototype),"firstUpdated",this).call(this,e),this._getBlueprints()}},{kind:"get",key:"_blueprint",value:function(){if(this._blueprints)return this._blueprints[this.config.use_blueprint.path]}},{kind:"method",key:"render",value:function(){var e,t;const i=this._blueprint;return l.dy`
      ${"off"===(null===(e=this.stateObj)||void 0===e?void 0:e.state)?l.dy`
            <ha-alert alert-type="info">
              ${this.hass.localize("ui.panel.config.automation.editor.disabled")}
              <mwc-button slot="action" @click=${this._enable}>
                ${this.hass.localize("ui.panel.config.automation.editor.enable")}
              </mwc-button>
            </ha-alert>
          `:""}
      ${this.config.description?l.dy`<p class="description">${this.config.description}</p>`:""}
      <ha-card
        outlined
        class="blueprint"
        .header=${this.hass.localize("ui.panel.config.automation.editor.blueprint.header")}
      >
        <div class="blueprint-picker-container">
          ${this._blueprints?Object.keys(this._blueprints).length?l.dy`
                  <ha-blueprint-picker
                    .hass=${this.hass}
                    .label=${this.hass.localize("ui.panel.config.automation.editor.blueprint.blueprint_to_use")}
                    .blueprints=${this._blueprints}
                    .value=${this.config.use_blueprint.path}
                    @value-changed=${this._blueprintChanged}
                  ></ha-blueprint-picker>
                `:this.hass.localize("ui.panel.config.automation.editor.blueprint.no_blueprints"):l.dy`<ha-circular-progress active></ha-circular-progress>`}
        </div>

        ${this.config.use_blueprint.path?i&&"error"in i?l.dy`<p class="warning padding">
                There is an error in this Blueprint: ${i.error}
              </p>`:l.dy`${null!=i&&i.metadata.description?l.dy`<ha-markdown
                    class="card-content"
                    breaks
                    .content=${i.metadata.description}
                  ></ha-markdown>`:""}
              ${null!=i&&null!==(t=i.metadata)&&void 0!==t&&t.input&&Object.keys(i.metadata.input).length?Object.entries(i.metadata.input).map((([e,t])=>{var i,r;return l.dy`<ha-settings-row .narrow=${this.narrow}>
                        <span slot="heading">${(null==t?void 0:t.name)||e}</span>
                        <ha-markdown
                          slot="description"
                          class="card-content"
                          breaks
                          .content=${null==t?void 0:t.description}
                        ></ha-markdown>
                        ${null!=t&&t.selector?l.dy`<ha-selector
                              .hass=${this.hass}
                              .selector=${t.selector}
                              .key=${e}
                              .value=${null!==(i=this.config.use_blueprint.input&&this.config.use_blueprint.input[e])&&void 0!==i?i:null==t?void 0:t.default}
                              @value-changed=${this._inputChanged}
                            ></ha-selector>`:l.dy`<ha-textfield
                              .key=${e}
                              required
                              .value=${null!==(r=this.config.use_blueprint.input&&this.config.use_blueprint.input[e])&&void 0!==r?r:null==t?void 0:t.default}
                              @input=${this._inputChanged}
                            ></ha-textfield>`}
                      </ha-settings-row>`})):l.dy`<p class="padding">
                    ${this.hass.localize("ui.panel.config.automation.editor.blueprint.no_inputs")}
                  </p>`}`:""}
      </ha-card>
    `}},{kind:"method",key:"_getBlueprints",value:async function(){this._blueprints=await(0,k.wc)(this.hass,"automation")}},{kind:"method",key:"_blueprintChanged",value:function(e){e.stopPropagation(),this.config.use_blueprint.path!==e.detail.value&&(0,d.B)(this,"value-changed",{value:Object.assign({},this.config,{use_blueprint:{path:e.detail.value}})})}},{kind:"method",key:"_inputChanged",value:function(e){var t;e.stopPropagation();const i=e.target,r=i.key,o=(null===(t=e.detail)||void 0===t?void 0:t.value)||i.value;if(this.config.use_blueprint.input&&this.config.use_blueprint.input[r]===o||!this.config.use_blueprint.input&&""===o)return;const n=Object.assign({},this.config.use_blueprint.input,{[r]:o});""!==o&&void 0!==o||delete n[r],(0,d.B)(this,"value-changed",{value:Object.assign({},this.config,{use_blueprint:Object.assign({},this.config.use_blueprint,{input:n})})})}},{kind:"method",key:"_enable",value:async function(){this.hass&&this.stateObj&&await this.hass.callService("automation","turn_on",{entity_id:this.stateObj.entity_id})}},{kind:"get",static:!0,key:"styles",value:function(){return[y.Qx,l.iv`
        :host {
          display: block;
        }
        ha-card.blueprint {
          margin: 0 auto;
        }
        .padding {
          padding: 16px;
        }
        .link-button-row {
          padding: 14px;
        }
        .blueprint-picker-container {
          padding: 0 16px 16px;
        }
        ha-textfield,
        ha-blueprint-picker {
          display: block;
        }
        h3 {
          margin: 16px;
        }
        .introduction {
          margin-top: 0;
          margin-bottom: 12px;
        }
        .introduction a {
          color: var(--primary-color);
        }
        p {
          margin-bottom: 0;
        }
        .description {
          margin-bottom: 16px;
        }
        ha-settings-row {
          --paper-time-input-justify-content: flex-end;
          --settings-row-content-width: 100%;
          --settings-row-prefix-display: contents;
          border-top: 1px solid var(--divider-color);
        }
        ha-alert {
          margin-bottom: 16px;
          display: block;
        }
      `]}}]}}),l.oi);var D=i(27322);i(44686),i(50364),i(4670);function M(){M=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var o=t.placement;if(t.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!j(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return F(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?F(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=H(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:I(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=I(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function T(e){var t,i=H(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function S(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function j(e){return e.decorators&&e.decorators.length}function V(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function I(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function H(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function F(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}const L="M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z";!function(e,t,i,r){var o=M();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),i),s=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var o,n=e[r];if("method"===n.kind&&(o=t.find(i)))if(V(n.descriptor)||V(o.descriptor)){if(j(n)||j(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(j(n)){if(j(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}S(n,o)}else t.push(n)}return t}(a.d.map(T)),e);o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,r.Mo)("manual-automation-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"config",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"stateObj",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,reflect:!0,attribute:"re-order-mode"})],key:"reOrderMode",value(){return!1}},{kind:"method",key:"render",value:function(){var e;return l.dy`
      ${"off"===(null===(e=this.stateObj)||void 0===e?void 0:e.state)?l.dy`
            <ha-alert alert-type="info">
              ${this.hass.localize("ui.panel.config.automation.editor.disabled")}
              <mwc-button slot="action" @click=${this._enable}>
                ${this.hass.localize("ui.panel.config.automation.editor.enable")}
              </mwc-button>
            </ha-alert>
          `:""}
      ${this.reOrderMode?l.dy`
            <ha-alert
              alert-type="info"
              .title=${this.hass.localize("ui.panel.config.automation.editor.re_order_mode.title")}
            >
              ${this.hass.localize("ui.panel.config.automation.editor.re_order_mode.description")}
              <mwc-button slot="action" @click=${this._exitReOrderMode}>
                ${this.hass.localize("ui.panel.config.automation.editor.re_order_mode.exit")}
              </mwc-button>
            </ha-alert>
          `:""}
      ${this.config.description?l.dy`<p class="description">${this.config.description}</p>`:""}
      <div class="header">
        <h2 id="triggers-heading" class="name">
          ${this.hass.localize("ui.panel.config.automation.editor.triggers.header")}
        </h2>
        <a
          href=${(0,D.R)(this.hass,"/docs/automation/trigger/")}
          target="_blank"
          rel="noreferrer"
        >
          <ha-icon-button
            .path=${L}
            .label=${this.hass.localize("ui.panel.config.automation.editor.triggers.learn_more")}
          ></ha-icon-button>
        </a>
      </div>

      <ha-automation-trigger
        role="region"
        aria-labelledby="triggers-heading"
        .triggers=${this.config.trigger}
        @value-changed=${this._triggerChanged}
        .hass=${this.hass}
        .reOrderMode=${this.reOrderMode}
      ></ha-automation-trigger>

      <div class="header">
        <h2 id="conditions-heading" class="name">
          ${this.hass.localize("ui.panel.config.automation.editor.conditions.header")}
        </h2>
        <a
          href=${(0,D.R)(this.hass,"/docs/automation/condition/")}
          target="_blank"
          rel="noreferrer"
        >
          <ha-icon-button
            .path=${L}
            .label=${this.hass.localize("ui.panel.config.automation.editor.conditions.learn_more")}
          ></ha-icon-button>
        </a>
      </div>

      <ha-automation-condition
        role="region"
        aria-labelledby="conditions-heading"
        .conditions=${this.config.condition||[]}
        @value-changed=${this._conditionChanged}
        .hass=${this.hass}
        .reOrderMode=${this.reOrderMode}
      ></ha-automation-condition>

      <div class="header">
        <h2 id="actions-heading" class="name">
          ${this.hass.localize("ui.panel.config.automation.editor.actions.header")}
        </h2>
        <div>
          <a
            href=${(0,D.R)(this.hass,"/docs/automation/action/")}
            target="_blank"
            rel="noreferrer"
          >
            <ha-icon-button
              .path=${L}
              .label=${this.hass.localize("ui.panel.config.automation.editor.actions.learn_more")}
            ></ha-icon-button>
          </a>
        </div>
      </div>

      <ha-automation-action
        role="region"
        aria-labelledby="actions-heading"
        .actions=${this.config.action}
        @value-changed=${this._actionChanged}
        .hass=${this.hass}
        .narrow=${this.narrow}
        .reOrderMode=${this.reOrderMode}
      ></ha-automation-action>
    `}},{kind:"method",key:"_exitReOrderMode",value:function(){this.reOrderMode=!this.reOrderMode}},{kind:"method",key:"_triggerChanged",value:function(e){e.stopPropagation(),(0,d.B)(this,"value-changed",{value:Object.assign({},this.config,{trigger:e.detail.value})})}},{kind:"method",key:"_conditionChanged",value:function(e){e.stopPropagation(),(0,d.B)(this,"value-changed",{value:Object.assign({},this.config,{condition:e.detail.value})})}},{kind:"method",key:"_actionChanged",value:function(e){e.stopPropagation(),(0,d.B)(this,"value-changed",{value:Object.assign({},this.config,{action:e.detail.value})})}},{kind:"method",key:"_enable",value:async function(){this.hass&&this.stateObj&&await this.hass.callService("automation","turn_on",{entity_id:this.stateObj.entity_id})}},{kind:"get",static:!0,key:"styles",value:function(){return[y.Qx,l.iv`
        :host {
          display: block;
        }
        ha-card {
          overflow: hidden;
        }
        .description {
          margin: 0;
        }
        p {
          margin-bottom: 0;
        }
        .header {
          display: flex;
          align-items: center;
        }
        .header:first-child {
          margin-top: -16px;
        }
        .header .name {
          font-size: 20px;
          font-weight: 400;
          flex: 1;
        }
        .header a {
          color: var(--secondary-text-color);
        }
        ha-alert {
          display: block;
          margin-bottom: 16px;
        }
      `]}}]}}),l.oi);function R(){R=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var o=t.placement;if(t.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!U(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return q(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?q(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=N(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:W(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=W(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function B(e){var t,i=N(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function Z(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function U(e){return e.decorators&&e.decorators.length}function Y(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function W(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function N(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function q(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function Q(){return Q="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=G(e)););return e}(e,t);if(r){var o=Object.getOwnPropertyDescriptor(r,t);return o.get?o.get.call(arguments.length<3?e:i):o.value}},Q.apply(this,arguments)}function G(e){return G=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},G(e)}const K="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z";let J=function(e,t,i,r){var o=R();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),i),s=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var o,n=e[r];if("method"===n.kind&&(o=t.find(i)))if(Y(n.descriptor)||Y(o.descriptor)){if(U(n)||U(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(U(n)){if(U(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}Z(n,o)}else t.push(n)}return t}(a.d.map(B)),e);return o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}(null,(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"automationId",value(){return null}},{kind:"field",decorators:[(0,r.Cb)()],key:"automations",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"route",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_dirty",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_errors",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_entityId",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_mode",value(){return"gui"}},{kind:"field",decorators:[(0,r.IO)("ha-yaml-editor",!0)],key:"_yamlEditor",value:void 0},{kind:"field",decorators:[(0,r.IO)("manual-automation-editor")],key:"_manualEditor",value:void 0},{kind:"field",key:"_configSubscriptions",value(){return{}}},{kind:"field",key:"_configSubscriptionsId",value(){return 1}},{kind:"method",key:"render",value:function(){var e;const t=this._entityId?this.hass.states[this._entityId]:void 0;return l.dy`
      <hass-subpage
        .hass=${this.hass}
        .narrow=${this.narrow}
        .route=${this.route}
        .backCallback=${this._backTapped}
        .header=${this._config?this._config.alias||this.hass.localize("ui.panel.config.automation.editor.default_name"):""}
      >
        ${null!==(e=this._config)&&void 0!==e&&e.id&&!this.narrow?l.dy`
              <mwc-button @click=${this._showTrace} slot="toolbar-icon">
                ${this.hass.localize("ui.panel.config.automation.editor.show_trace")}
              </mwc-button>
            `:""}
        <ha-button-menu corner="BOTTOM_START" slot="toolbar-icon">
          <ha-icon-button
            slot="trigger"
            .label=${this.hass.localize("ui.common.menu")}
            .path=${"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z"}
          ></ha-icon-button>

          <mwc-list-item
            graphic="icon"
            .disabled=${!t}
            @click=${this._showInfo}
          >
            ${this.hass.localize("ui.panel.config.automation.editor.show_info")}
            <ha-svg-icon
              slot="graphic"
              .path=${"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z"}
            ></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            graphic="icon"
            .disabled=${!t}
            @click=${this._runActions}
          >
            ${this.hass.localize("ui.panel.config.automation.editor.run")}
            <ha-svg-icon slot="graphic" .path=${"M8,5.14V19.14L19,12.14L8,5.14Z"}></ha-svg-icon>
          </mwc-list-item>

          ${t&&this._config&&this.narrow?l.dy`<a href="/config/automation/trace/${this._config.id}">
                <mwc-list-item graphic="icon">
                  ${this.hass.localize("ui.panel.config.automation.editor.show_trace")}
                  <ha-svg-icon
                    slot="graphic"
                    .path=${"M15,12C15,10.7 14.16,9.6 13,9.18V6.82C14.16,6.4 15,5.3 15,4A3,3 0 0,0 12,1A3,3 0 0,0 9,4C9,5.3 9.84,6.4 11,6.82V9.19C9.84,9.6 9,10.7 9,12C9,13.3 9.84,14.4 11,14.82V17.18C9.84,17.6 9,18.7 9,20A3,3 0 0,0 12,23A3,3 0 0,0 15,20C15,18.7 14.16,17.6 13,17.18V14.82C14.16,14.4 15,13.3 15,12M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M12,21A1,1 0 0,1 11,20A1,1 0 0,1 12,19A1,1 0 0,1 13,20A1,1 0 0,1 12,21Z"}
                  ></ha-svg-icon>
                </mwc-list-item>
              </a>`:""}

          <mwc-list-item
            graphic="icon"
            @click=${this._promptAutomationAlias}
            .disabled=${!this.automationId||"yaml"===this._mode}
          >
            ${this.hass.localize("ui.panel.config.automation.editor.rename")}
            <ha-svg-icon slot="graphic" .path=${"M18,17H10.5L12.5,15H18M6,17V14.5L13.88,6.65C14.07,6.45 14.39,6.45 14.59,6.65L16.35,8.41C16.55,8.61 16.55,8.92 16.35,9.12L8.47,17M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z"}></ha-svg-icon>
          </mwc-list-item>

          ${this._config&&!("use_blueprint"in this._config)?l.dy`
                <mwc-list-item
                  graphic="icon"
                  @click=${this._promptAutomationMode}
                  .disabled=${"yaml"===this._mode}
                >
                  ${this.hass.localize("ui.panel.config.automation.editor.change_mode")}
                  <ha-svg-icon
                    slot="graphic"
                    .path=${"M12,14A2,2 0 0,1 14,16A2,2 0 0,1 12,18A2,2 0 0,1 10,16A2,2 0 0,1 12,14M23.46,8.86L21.87,15.75L15,14.16L18.8,11.78C17.39,9.5 14.87,8 12,8C8.05,8 4.77,10.86 4.12,14.63L2.15,14.28C2.96,9.58 7.06,6 12,6C15.58,6 18.73,7.89 20.5,10.72L23.46,8.86Z"}
                  ></ha-svg-icon>
                </mwc-list-item>
              `:""}
          ${this._config&&!("use_blueprint"in this._config)?l.dy`<mwc-list-item
                graphic="icon"
                @click=${this._toggleReOrderMode}
                .disabled=${"yaml"===this._mode}
              >
                ${this.hass.localize("ui.panel.config.automation.editor.re_order")}
                <ha-svg-icon slot="graphic" .path=${"M18 21L14 17H17V7H14L18 3L22 7H19V17H22M2 19V17H12V19M2 13V11H9V13M2 7V5H6V7H2Z"}></ha-svg-icon>
              </mwc-list-item>`:""}

          <mwc-list-item
            .disabled=${!this.automationId}
            graphic="icon"
            @click=${this._duplicate}
          >
            ${this.hass.localize("ui.panel.config.automation.picker.duplicate")}
            <ha-svg-icon
              slot="graphic"
              .path=${"M11,17H4A2,2 0 0,1 2,15V3A2,2 0 0,1 4,1H16V3H4V15H11V13L15,16L11,19V17M19,21V7H8V13H6V7A2,2 0 0,1 8,5H19A2,2 0 0,1 21,7V21A2,2 0 0,1 19,23H8A2,2 0 0,1 6,21V19H8V21H19Z"}
            ></ha-svg-icon>
          </mwc-list-item>

          <li divider role="separator"></li>

          <mwc-list-item graphic="icon" @click=${this._switchUiMode}>
            ${this.hass.localize("ui.panel.config.automation.editor.edit_ui")}
            ${"gui"===this._mode?l.dy`<ha-svg-icon
                  class="selected_menu_item"
                  slot="graphic"
                  .path=${K}
                ></ha-svg-icon>`:""}
          </mwc-list-item>
          <mwc-list-item graphic="icon" @click=${this._switchYamlMode}>
            ${this.hass.localize("ui.panel.config.automation.editor.edit_yaml")}
            ${"yaml"===this._mode?l.dy`<ha-svg-icon
                  class="selected_menu_item"
                  slot="graphic"
                  .path=${K}
                ></ha-svg-icon>`:""}
          </mwc-list-item>

          <li divider role="separator"></li>

          <mwc-list-item
            graphic="icon"
            .disabled=${!t}
            @click=${this._toggle}
          >
            ${"off"===(null==t?void 0:t.state)?this.hass.localize("ui.panel.config.automation.editor.enable"):this.hass.localize("ui.panel.config.automation.editor.disable")}
            <ha-svg-icon
              slot="graphic"
              .path=${"off"===(null==t?void 0:t.state)?"M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M10,16.5L16,12L10,7.5V16.5Z":"M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4M9,9V15H15V9"}
            ></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            .disabled=${!this.automationId}
            class=${(0,c.$)({warning:Boolean(this.automationId)})}
            graphic="icon"
            @click=${this._deleteConfirm}
          >
            ${this.hass.localize("ui.panel.config.automation.picker.delete")}
            <ha-svg-icon
              class=${(0,c.$)({warning:Boolean(this.automationId)})}
              slot="graphic"
              .path=${"M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"}
            >
            </ha-svg-icon>
          </mwc-list-item>
        </ha-button-menu>

        ${this._config?l.dy`
              <div
                class="content ${(0,c.$)({"yaml-mode":"yaml"===this._mode})}"
                @subscribe-automation-config=${this._subscribeAutomationConfig}
              >
                ${this._errors?l.dy`<ha-alert alert-type="error">
                      ${this._errors}
                    </ha-alert>`:""}
                ${"gui"===this._mode?"use_blueprint"in this._config?l.dy`
                        <blueprint-automation-editor
                          .hass=${this.hass}
                          .narrow=${this.narrow}
                          .isWide=${this.isWide}
                          .stateObj=${t}
                          .config=${this._config}
                          @value-changed=${this._valueChanged}
                        ></blueprint-automation-editor>
                      `:l.dy`
                        <manual-automation-editor
                          .hass=${this.hass}
                          .narrow=${this.narrow}
                          .isWide=${this.isWide}
                          .stateObj=${t}
                          .config=${this._config}
                          @value-changed=${this._valueChanged}
                        ></manual-automation-editor>
                      `:"yaml"===this._mode?l.dy`
                      ${"off"===(null==t?void 0:t.state)?l.dy`
                            <ha-alert alert-type="info">
                              ${this.hass.localize("ui.panel.config.automation.editor.disabled")}
                              <mwc-button slot="action" @click=${this._toggle}>
                                ${this.hass.localize("ui.panel.config.automation.editor.enable")}
                              </mwc-button>
                            </ha-alert>
                          `:""}
                      <ha-yaml-editor
                        .hass=${this.hass}
                        .defaultValue=${this._preprocessYaml()}
                        @value-changed=${this._yamlChanged}
                      ></ha-yaml-editor>
                      <ha-card outlined>
                        <div class="card-actions">
                          <mwc-button @click=${this._copyYaml}>
                            ${this.hass.localize("ui.panel.config.automation.editor.copy_to_clipboard")}
                          </mwc-button>
                        </div>
                      </ha-card>
                    `:""}
              </div>
            `:""}
        <ha-fab
          slot="fab"
          class=${(0,c.$)({dirty:this._dirty})}
          .label=${this.hass.localize("ui.panel.config.automation.editor.save")}
          extended
          @click=${this._saveAutomation}
        >
          <ha-svg-icon slot="icon" .path=${"M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z"}></ha-svg-icon>
        </ha-fab>
      </hass-subpage>
    `}},{kind:"method",key:"updated",value:function(e){Q(G(i.prototype),"updated",this).call(this,e);const t=e.get("automationId");if(e.has("automationId")&&this.automationId&&this.hass&&t!==this.automationId&&(this._setEntityId(),this._loadConfig()),e.has("automationId")&&!this.automationId&&this.hass){const e=(0,p.Pl)();let t={description:""};e&&"use_blueprint"in e||(t=Object.assign({},t,{mode:"single",trigger:[],condition:[],action:[]})),this._config=Object.assign({},t,e),this._entityId=void 0,this._dirty=!0}e.has("automations")&&this.automationId&&!this._entityId&&this._setEntityId(),e.has("_config")&&Object.values(this._configSubscriptions).forEach((e=>e(this._config)))}},{kind:"method",key:"_setEntityId",value:function(){const e=this.automations.find((e=>e.attributes.id===this.automationId));this._entityId=null==e?void 0:e.entity_id}},{kind:"method",key:"_loadConfig",value:async function(){try{const e=await(0,p.cV)(this.hass,this.automationId);for(const t of["trigger","condition","action"]){const i=e[t];i&&!Array.isArray(i)&&(e[t]=[i])}this._dirty=!1,this._config=e}catch(e){await(0,f.Ys)(this,{text:404===e.status_code?this.hass.localize("ui.panel.config.automation.editor.load_error_not_editable"):this.hass.localize("ui.panel.config.automation.editor.load_error_unknown","err_no",e.status_code)}),history.back()}}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation(),this._config=e.detail.value,this._dirty=!0,this._errors=void 0}},{kind:"method",key:"_showInfo",value:function(){this.hass&&this._entityId&&(0,d.B)(this,"hass-more-info",{entityId:this._entityId})}},{kind:"method",key:"_showTrace",value:async function(){var e;if(null!==(e=this._config)&&void 0!==e&&e.id){await this.confirmUnsavedChanged()&&(0,u.c)(`/config/automation/trace/${this._config.id}`)}}},{kind:"method",key:"_runActions",value:function(){this.hass&&this._entityId&&(0,p.Es)(this.hass,this.hass.states[this._entityId].entity_id)}},{kind:"method",key:"_toggle",value:async function(){if(!this.hass||!this._entityId)return;const e=this.hass.states[this._entityId],t="off"===e.state?"turn_on":"turn_off";await this.hass.callService("automation",t,{entity_id:e.entity_id})}},{kind:"method",key:"_preprocessYaml",value:function(){if(!this._config)return{};const e=Object.assign({},this._config);return delete e.id,e}},{kind:"method",key:"_copyYaml",value:async function(){var e;null!==(e=this._yamlEditor)&&void 0!==e&&e.yaml&&(await(0,h.v)(this._yamlEditor.yaml),(0,v.C)(this,{message:this.hass.localize("ui.common.copied_clipboard")}))}},{kind:"method",key:"_yamlChanged",value:function(e){var t;e.stopPropagation(),e.detail.isValid&&(this._config=Object.assign({id:null===(t=this._config)||void 0===t?void 0:t.id},e.detail.value),this._errors=void 0,this._dirty=!0)}},{kind:"method",key:"confirmUnsavedChanged",value:async function(){return!this._dirty||(0,f.g7)(this,{text:this.hass.localize("ui.panel.config.automation.editor.unsaved_confirm"),confirmText:this.hass.localize("ui.common.leave"),dismissText:this.hass.localize("ui.common.stay")})}},{kind:"field",key:"_backTapped",value(){return async()=>{await this.confirmUnsavedChanged()&&history.back()}}},{kind:"method",key:"_duplicate",value:async function(){await this.confirmUnsavedChanged()&&(0,p.Ip)(Object.assign({},this._config,{id:void 0,alias:void 0}))}},{kind:"method",key:"_deleteConfirm",value:async function(){(0,f.g7)(this,{text:this.hass.localize("ui.panel.config.automation.picker.delete_confirm"),confirmText:this.hass.localize("ui.common.delete"),dismissText:this.hass.localize("ui.common.cancel"),confirm:()=>this._delete()})}},{kind:"method",key:"_delete",value:async function(){this.automationId&&(await(0,p.SC)(this.hass,this.automationId),history.back())}},{kind:"method",key:"_switchUiMode",value:function(){this._mode="gui"}},{kind:"method",key:"_switchYamlMode",value:function(){this._mode="yaml"}},{kind:"method",key:"_toggleReOrderMode",value:function(){this._manualEditor&&(this._manualEditor.reOrderMode=!this._manualEditor.reOrderMode)}},{kind:"method",key:"_promptAutomationAlias",value:async function(){return new Promise((e=>{var t,i;t=this,i={config:this._config,updateAutomation:t=>{this._config=t,this._dirty=!0,this.requestUpdate(),e()},onClose:()=>e()},(0,d.B)(t,"show-dialog",{dialogTag:"ha-dialog-automation-rename",dialogImport:b,dialogParams:i})}))}},{kind:"method",key:"_promptAutomationMode",value:async function(){return new Promise((e=>{var t,i;t=this,i={config:this._config,updateAutomation:t=>{this._config=t,this._dirty=!0,this.requestUpdate(),e()},onClose:()=>e()},(0,d.B)(t,"show-dialog",{dialogTag:"ha-dialog-automation-mode",dialogImport:g,dialogParams:i})}))}},{kind:"method",key:"_saveAutomation",value:async function(){const e=this.automationId||String(Date.now());this.automationId||await this._promptAutomationAlias();try{await(0,p.sq)(this.hass,e,this._config)}catch(t){throw this._errors=t.body.message||t.error||t.body,(0,v.C)(this,{message:t.body.message||t.error||t.body}),t}this._dirty=!1,this.automationId||(0,u.c)(`/config/automation/edit/${e}`,{replace:!0})}},{kind:"method",key:"_subscribeAutomationConfig",value:function(e){const t=this._configSubscriptionsId++;this._configSubscriptions[t]=e.detail.callback,e.detail.unsub=()=>{delete this._configSubscriptions[t]},e.detail.callback(this._config)}},{kind:"method",key:"handleKeyboardSave",value:function(){this._saveAutomation()}},{kind:"get",static:!0,key:"styles",value:function(){return[y.Qx,l.iv`
        ha-card {
          overflow: hidden;
        }
        .content {
          padding-bottom: 20px;
        }
        .yaml-mode {
          height: 100%;
          display: flex;
          flex-direction: column;
          padding-bottom: 0;
        }
        manual-automation-editor,
        blueprint-automation-editor {
          margin: 0 auto;
          max-width: 1040px;
          padding: 28px 20px 0;
        }
        ha-yaml-editor {
          flex-grow: 1;
          --code-mirror-height: 100%;
          min-height: 0;
        }
        .yaml-mode ha-card {
          overflow: initial;
          --ha-card-border-radius: 0;
          border-bottom: 1px solid var(--divider-color);
        }
        p {
          margin-bottom: 0;
        }
        ha-entity-toggle {
          margin-right: 8px;
        }
        ha-fab {
          position: relative;
          bottom: calc(-80px - env(safe-area-inset-bottom));
          transition: bottom 0.3s;
        }
        ha-fab.dirty {
          bottom: 0;
        }
        .selected_menu_item {
          color: var(--primary-color);
        }
        li[role="separator"] {
          border-bottom-color: var(--divider-color);
        }
        ha-button-menu a {
          text-decoration: none;
          color: var(--primary-color);
        }
        h1 {
          margin: 0;
        }
        .header-name {
          display: flex;
          align-items: center;
          margin: 0 auto;
          max-width: 1040px;
          padding: 28px 20px 0;
        }
      `]}}]}}),(0,m.U)(l.oi));customElements.define("ha-automation-editor",J);i(54444);var X=i(7323),ee=i(44583),te=i(5435),ie=i(91741),re=(i(67556),i(88324),i(48429),i(96551),i(29311));const oe=()=>Promise.all([i.e(85084),i.e(42228)]).then(i.bind(i,42228));function ne(){ne=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var o=t.placement;if(t.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!le(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return he(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?he(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=ue(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:de(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=de(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function ae(e){var t,i=ue(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function se(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function le(e){return e.decorators&&e.decorators.length}function ce(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function de(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function ue(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function he(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}const pe=864e5;!function(e,t,i,r){var o=ne();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),i),s=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var o,n=e[r];if("method"===n.kind&&(o=t.find(i)))if(ce(n.descriptor)||ce(o.descriptor)){if(le(n)||le(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(le(n)){if(le(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}se(n,o)}else t.push(n)}return t}(a.d.map(ae)),e);o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,r.Mo)("ha-automation-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"route",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"automations",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"_activeFilters",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_filteredAutomations",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_filterValue",value:void 0},{kind:"field",key:"_automations",value(){return(0,o.Z)(((e,t)=>null===t?[]:(t?e.filter((e=>t.includes(e.entity_id))):e).map((e=>Object.assign({},e,{name:(0,ie.C)(e),last_triggered:e.attributes.last_triggered||void 0,disabled:"off"===e.state})))))}},{kind:"field",key:"_columns",value(){return(0,o.Z)(((e,t)=>{const i={name:{title:this.hass.localize("ui.panel.config.automation.picker.headers.name"),sortable:!0,filterable:!0,direction:"asc",grows:!0,template:e?(e,t)=>{const i=new Date(t.attributes.last_triggered),r=((new Date).getTime()-i.getTime())/pe;return l.dy`
                  ${e}
                  <div class="secondary">
                    ${this.hass.localize("ui.card.automation.last_triggered")}:
                    ${t.attributes.last_triggered?r>3?(0,ee.yD)(i,this.hass.locale):(0,te.G)(i,this.hass.locale):this.hass.localize("ui.components.relative_time.never")}
                  </div>
                `}:void 0}};return e||(i.last_triggered={sortable:!0,width:"20%",title:this.hass.localize("ui.card.automation.last_triggered"),template:e=>{const t=new Date(e),i=((new Date).getTime()-t.getTime())/pe;return l.dy`
              ${e?i>3?(0,ee.yD)(t,this.hass.locale):(0,te.G)(t,this.hass.locale):this.hass.localize("ui.components.relative_time.never")}
            `}}),i.disabled=this.narrow?{title:"",template:e=>e?l.dy`
                    <paper-tooltip animation-delay="0" position="left">
                      ${this.hass.localize("ui.panel.config.automation.picker.disabled")}
                    </paper-tooltip>
                    <ha-svg-icon
                      .path=${"M12 2C17.5 2 22 6.5 22 12S17.5 22 12 22 2 17.5 2 12 6.5 2 12 2M12 4C10.1 4 8.4 4.6 7.1 5.7L18.3 16.9C19.3 15.5 20 13.8 20 12C20 7.6 16.4 4 12 4M16.9 18.3L5.7 7.1C4.6 8.4 4 10.1 4 12C4 16.4 7.6 20 12 20C13.9 20 15.6 19.4 16.9 18.3Z"}
                      style="color: var(--secondary-text-color)"
                    ></ha-svg-icon>
                  `:""}:{width:"20%",title:"",template:e=>e?l.dy`
                    <ha-chip>
                      ${this.hass.localize("ui.panel.config.automation.picker.disabled")}
                    </ha-chip>
                  `:""},i.actions={title:"",width:this.narrow?void 0:"10%",type:"overflow-menu",template:(e,t)=>l.dy`
            <ha-icon-overflow-menu
              .hass=${this.hass}
              narrow
              .items=${[{path:"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z",label:this.hass.localize("ui.panel.config.automation.editor.show_info"),action:()=>this._showInfo(t)},{path:"M8,5.14V19.14L19,12.14L8,5.14Z",label:this.hass.localize("ui.panel.config.automation.editor.run"),action:()=>this._runActions(t)},{path:"M15,12C15,10.7 14.16,9.6 13,9.18V6.82C14.16,6.4 15,5.3 15,4A3,3 0 0,0 12,1A3,3 0 0,0 9,4C9,5.3 9.84,6.4 11,6.82V9.19C9.84,9.6 9,10.7 9,12C9,13.3 9.84,14.4 11,14.82V17.18C9.84,17.6 9,18.7 9,20A3,3 0 0,0 12,23A3,3 0 0,0 15,20C15,18.7 14.16,17.6 13,17.18V14.82C14.16,14.4 15,13.3 15,12M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M12,21A1,1 0 0,1 11,20A1,1 0 0,1 12,19A1,1 0 0,1 13,20A1,1 0 0,1 12,21Z",label:this.hass.localize("ui.panel.config.automation.editor.show_trace"),action:()=>this._showTrace(t)},{divider:!0},{path:"M11,17H4A2,2 0 0,1 2,15V3A2,2 0 0,1 4,1H16V3H4V15H11V13L15,16L11,19V17M19,21V7H8V13H6V7A2,2 0 0,1 8,5H19A2,2 0 0,1 21,7V21A2,2 0 0,1 19,23H8A2,2 0 0,1 6,21V19H8V21H19Z",label:this.hass.localize("ui.panel.config.automation.picker.duplicate"),action:()=>this.duplicate(t)},{path:"off"===t.state?"M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M10,16.5L16,12L10,7.5V16.5Z":"M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4M9,9V15H15V9",label:"off"===t.state?this.hass.localize("ui.panel.config.automation.editor.enable"):this.hass.localize("ui.panel.config.automation.editor.disable"),action:()=>this._toggle(t)},{label:this.hass.localize("ui.panel.config.automation.picker.delete"),path:"M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",action:()=>this._deleteConfirm(t),warning:!0}]}
            >
            </ha-icon-overflow-menu>
          `},i}))}},{kind:"method",key:"render",value:function(){return l.dy`
      <hass-tabs-subpage-data-table
        .hass=${this.hass}
        .narrow=${this.narrow}
        back-path="/config"
        id="entity_id"
        .route=${this.route}
        .tabs=${re.configSections.automations}
        .activeFilters=${this._activeFilters}
        .columns=${this._columns(this.narrow,this.hass.locale)}
        .data=${this._automations(this.automations,this._filteredAutomations)}
        @row-click=${this._handleRowClicked}
        .noDataText=${this.hass.localize("ui.panel.config.automation.picker.no_automations")}
        @clear-filter=${this._clearFilter}
        hasFab
        clickable
      >
        <ha-icon-button
          slot="toolbar-icon"
          .label=${this.hass.localize("ui.common.help")}
          .path=${"M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z"}
          @click=${this._showHelp}
        ></ha-icon-button>
        <ha-button-related-filter-menu
          slot="filter-menu"
          corner="BOTTOM_START"
          .narrow=${this.narrow}
          .hass=${this.hass}
          .value=${this._filterValue}
          exclude-domains='["automation"]'
          @related-changed=${this._relatedFilterChanged}
        >
        </ha-button-related-filter-menu>
        <ha-fab
          slot="fab"
          .label=${this.hass.localize("ui.panel.config.automation.picker.add_automation")}
          extended
          @click=${this._createNew}
        >
          <ha-svg-icon slot="icon" .path=${"M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"}></ha-svg-icon>
        </ha-fab>
      </hass-tabs-subpage-data-table>
    `}},{kind:"method",key:"_relatedFilterChanged",value:function(e){this._filterValue=e.detail.value,this._filterValue?(this._activeFilters=[e.detail.filter],this._filteredAutomations=e.detail.items.automation||null):this._clearFilter()}},{kind:"method",key:"_clearFilter",value:function(){this._filteredAutomations=void 0,this._activeFilters=void 0,this._filterValue=void 0}},{kind:"method",key:"_showInfo",value:function(e){(0,d.B)(this,"hass-more-info",{entityId:e.entity_id})}},{kind:"method",key:"_runActions",value:function(e){(0,p.Es)(this.hass,e.entity_id)}},{kind:"method",key:"_showTrace",value:function(e){(0,u.c)(`/config/automation/trace/${e.attributes.id}`)}},{kind:"method",key:"_toggle",value:async function(e){const t="off"===e.state?"turn_on":"turn_off";await this.hass.callService("automation",t,{entity_id:e.entity_id})}},{kind:"method",key:"_deleteConfirm",value:async function(e){(0,f.g7)(this,{text:this.hass.localize("ui.panel.config.automation.picker.delete_confirm"),confirmText:this.hass.localize("ui.common.delete"),dismissText:this.hass.localize("ui.common.cancel"),confirm:()=>this._delete(e)})}},{kind:"method",key:"_delete",value:async function(e){try{await(0,p.SC)(this.hass,e.attributes.id)}catch(t){await(0,f.Ys)(this,{text:400===t.status_code?this.hass.localize("ui.panel.config.automation.editor.load_error_not_deletable"):this.hass.localize("ui.panel.config.automation.editor.load_error_unknown","err_no",t.status_code)})}}},{kind:"method",key:"duplicate",value:async function(e){try{const t=await(0,p.cV)(this.hass,e.attributes.id);(0,p.HF)(t)}catch(t){await(0,f.Ys)(this,{text:404===t.status_code?this.hass.localize("ui.panel.config.automation.editor.load_error_not_duplicable"):this.hass.localize("ui.panel.config.automation.editor.load_error_unknown","err_no",t.status_code)})}}},{kind:"method",key:"_showHelp",value:function(){(0,f.Ys)(this,{title:this.hass.localize("ui.panel.config.automation.caption"),text:l.dy`
        ${this.hass.localize("ui.panel.config.automation.picker.introduction")}
        <p>
          <a
            href=${(0,D.R)(this.hass,"/docs/automation/editor/")}
            target="_blank"
            rel="noreferrer"
          >
            ${this.hass.localize("ui.panel.config.automation.picker.learn_more")}
          </a>
        </p>
      `})}},{kind:"method",key:"_handleRowClicked",value:function(e){const t=this.automations.find((t=>t.entity_id===e.detail.id));null!=t&&t.attributes.id&&(0,u.c)(`/config/automation/edit/${t.attributes.id}`)}},{kind:"method",key:"_createNew",value:function(){var e;(0,X.p)(this.hass,"blueprint")?(e=this,(0,d.B)(e,"show-dialog",{dialogTag:"ha-dialog-new-automation",dialogImport:oe,dialogParams:{}})):(0,u.c)("/config/automation/edit/new")}},{kind:"get",static:!0,key:"styles",value:function(){return y.Qx}}]}}),l.oi);function fe(){fe=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var o=t.placement;if(t.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!ve(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return we(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?we(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=ke(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:be(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=be(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function me(e){var t,i=ke(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function ye(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function ve(e){return e.decorators&&e.decorators.length}function ge(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function be(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function ke(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function we(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function _e(){return _e="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=Ee(e)););return e}(e,t);if(r){var o=Object.getOwnPropertyDescriptor(r,t);return o.get?o.get.call(arguments.length<3?e:i):o.value}},_e.apply(this,arguments)}function Ee(e){return Ee=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},Ee(e)}!function(e,t,i,r){var o=fe();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),i),s=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var o,n=e[r];if("method"===n.kind&&(o=t.find(i)))if(ge(n.descriptor)||ge(o.descriptor)){if(ve(n)||ve(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(ve(n)){if(ve(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}ye(n,o)}else t.push(n)}return t}(a.d.map(me)),e);o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,r.Mo)("ha-config-automation")],(function(e,t){class s extends t{constructor(...t){super(...t),e(this)}}return{F:s,d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"showAdvanced",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"automations",value(){return[]}},{kind:"field",key:"_debouncedUpdateAutomations",value(){return(0,a.D)((e=>{const t=this._getAutomations(this.hass.states);var i,r;i=t,r=e.automations,i.length===r.length&&i.every(((e,t)=>e===r[t]))||(e.automations=t)}),10)}},{kind:"field",key:"routerOptions",value(){return{defaultPage:"dashboard",routes:{dashboard:{tag:"ha-automation-picker",cache:!0},edit:{tag:"ha-automation-editor"},trace:{tag:"ha-automation-trace",load:()=>Promise.all([i.e(99528),i.e(15246),i.e(53890)]).then(i.bind(i,53890))}}}}},{kind:"field",key:"_getAutomations",value(){return(0,o.Z)((e=>Object.values(e).filter((e=>"automation"===(0,n.N)(e)&&!e.attributes.restored))))}},{kind:"method",key:"firstUpdated",value:function(e){_e(Ee(s.prototype),"firstUpdated",this).call(this,e),this.hass.loadBackendTranslation("device_automation")}},{kind:"method",key:"updatePageEl",value:function(e,t){if(e.hass=this.hass,e.narrow=this.narrow,e.isWide=this.isWide,e.route=this.routeTail,e.showAdvanced=this.showAdvanced,this.hass&&(e.automations&&t?t.has("hass")&&this._debouncedUpdateAutomations(e):e.automations=this._getAutomations(this.hass.states)),(!t||t.has("route"))&&"dashboard"!==this._currentPage){const t=decodeURIComponent(this.routeTail.path.substr(1));e.automationId="new"===t?null:t}}}]}}),s.n)}}]);
//# sourceMappingURL=77912640.js.map