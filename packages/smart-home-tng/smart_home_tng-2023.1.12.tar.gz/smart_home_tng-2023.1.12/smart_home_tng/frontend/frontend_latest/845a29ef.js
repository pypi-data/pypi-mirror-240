"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[50850],{19267:(e,t,i)=>{i.a(e,(async(e,t)=>{try{var r=i(37500),n=i(36924),o=i(47181),s=(i(13266),i(22098),i(31206),i(4940),i(3555),i(25727)),a=(i(14089),i(86490)),l=i(11654),c=(i(88165),e([s]));function d(e,t,i,r){var n=h();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(f(s.d.map(p)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function h(){h=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!m(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,C(t)||E(t)||w(t)||k()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=g(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:v(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=v(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function p(e){var t,i=g(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function u(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function f(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(y(o.descriptor)||y(n.descriptor)){if(m(o)||m(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(m(o)){if(m(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}u(o,n)}else t.push(o)}return t}function m(e){return e.decorators&&e.decorators.length}function y(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function v(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function g(e){var t=b(e,"string");return"symbol"==typeof t?t:String(t)}function b(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function k(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function w(e,t){if(e){if("string"==typeof e)return _(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?_(e,t):void 0}}function _(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function E(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function C(e){if(Array.isArray(e))return e}function A(){return A="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=$(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},A.apply(this,arguments)}function $(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=x(e)););return e}function x(e){return x=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},x(e)}s=(c.then?(await c)():c)[0];d([(0,n.Mo)("blueprint-script-editor")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"config",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_blueprints",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){A(x(i.prototype),"firstUpdated",this).call(this,e),this._getBlueprints()}},{kind:"get",key:"_blueprint",value:function(){if(this._blueprints)return this._blueprints[this.config.use_blueprint.path]}},{kind:"method",key:"render",value:function(){var e;const t=this._blueprint;return r.dy`
      <ha-card
        outlined
        class="blueprint"
        .header=${this.hass.localize("ui.panel.config.automation.editor.blueprint.header")}
      >
        <div class="blueprint-picker-container">
          ${this._blueprints?Object.keys(this._blueprints).length?r.dy`
                  <ha-blueprint-picker
                    .hass=${this.hass}
                    .label=${this.hass.localize("ui.panel.config.automation.editor.blueprint.blueprint_to_use")}
                    .blueprints=${this._blueprints}
                    .value=${this.config.use_blueprint.path}
                    @value-changed=${this._blueprintChanged}
                  ></ha-blueprint-picker>
                `:this.hass.localize("ui.panel.config.automation.editor.blueprint.no_blueprints"):r.dy`<ha-circular-progress active></ha-circular-progress>`}
        </div>

        ${this.config.use_blueprint.path?t&&"error"in t?r.dy`<p class="warning padding">
                There is an error in this Blueprint: ${t.error}
              </p>`:r.dy`${null!=t&&t.metadata.description?r.dy`<ha-markdown
                    class="card-content"
                    breaks
                    .content=${t.metadata.description}
                  ></ha-markdown>`:""}
              ${null!=t&&null!==(e=t.metadata)&&void 0!==e&&e.input&&Object.keys(t.metadata.input).length?Object.entries(t.metadata.input).map((([e,t])=>{var i,n;return r.dy`<ha-settings-row .narrow=${this.narrow}>
                        <span slot="heading">${(null==t?void 0:t.name)||e}</span>
                        <span slot="description">${null==t?void 0:t.description}</span>
                        ${null!=t&&t.selector?r.dy`<ha-selector
                              .hass=${this.hass}
                              .selector=${t.selector}
                              .key=${e}
                              .value=${null!==(i=this.config.use_blueprint.input&&this.config.use_blueprint.input[e])&&void 0!==i?i:null==t?void 0:t.default}
                              @value-changed=${this._inputChanged}
                            ></ha-selector>`:r.dy`<ha-textfield
                              .key=${e}
                              required
                              .value=${null!==(n=this.config.use_blueprint.input&&this.config.use_blueprint.input[e])&&void 0!==n?n:null==t?void 0:t.default}
                              @change=${this._inputChanged}
                            ></ha-textfield>`}
                      </ha-settings-row>`})):r.dy`<p class="padding">
                    ${this.hass.localize("ui.panel.config.automation.editor.blueprint.no_inputs")}
                  </p>`}`:""}
      </ha-card>
    `}},{kind:"method",key:"_getBlueprints",value:async function(){this._blueprints=await(0,a.wc)(this.hass,"script")}},{kind:"method",key:"_blueprintChanged",value:function(e){e.stopPropagation(),this.config.use_blueprint.path!==e.detail.value&&(0,o.B)(this,"value-changed",{value:{...this.config,use_blueprint:{path:e.detail.value}}})}},{kind:"method",key:"_inputChanged",value:function(e){var t,i;e.stopPropagation();const r=e.target,n=r.key,s=null!==(t=null===(i=e.detail)||void 0===i?void 0:i.value)&&void 0!==t?t:r.value;if(this.config.use_blueprint.input&&this.config.use_blueprint.input[n]===s||!this.config.use_blueprint.input&&""===s)return;const a={...this.config.use_blueprint.input,[n]:s};""!==s&&void 0!==s||delete a[n],(0,o.B)(this,"value-changed",{value:{...this.config,use_blueprint:{...this.config.use_blueprint,input:a}}})}},{kind:"get",static:!0,key:"styles",value:function(){return[l.Qx,r.iv`
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
      `]}}]}}),r.oi);t()}catch(P){t(P)}}))},50850:(e,t,i)=>{i.a(e,(async(e,r)=>{try{i.r(t);var n=i(36924),o=i(14516),s=i(22311),a=i(38346),l=i(18199),c=i(67826),d=i(25931),h=e([c,d]);function p(e,t,i,r){var n=u();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(y(s.d.map(f)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function u(){u=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!v(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,$(t)||A(t)||E(t)||_()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=k(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:b(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=b(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function f(e){var t,i=k(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function m(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function y(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(g(o.descriptor)||g(n.descriptor)){if(v(o)||v(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(v(o)){if(v(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}m(o,n)}else t.push(o)}return t}function v(e){return e.decorators&&e.decorators.length}function g(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function b(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function k(e){var t=w(e,"string");return"symbol"==typeof t?t:String(t)}function w(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function _(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function E(e,t){if(e){if("string"==typeof e)return C(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?C(e,t):void 0}}function C(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function A(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function $(e){if(Array.isArray(e))return e}function x(){return x="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=P(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},x.apply(this,arguments)}function P(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=z(e)););return e}function z(e){return z=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},z(e)}[c,d]=h.then?(await h)():h;const D=(e,t)=>e.length===t.length&&e.every(((e,i)=>e===t[i]));p([(0,n.Mo)("ha-config-script")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"showAdvanced",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"scripts",value:()=>[]},{kind:"field",key:"routerOptions",value:()=>({defaultPage:"dashboard",routes:{dashboard:{tag:"ha-script-picker",cache:!0},edit:{tag:"ha-script-editor"},trace:{tag:"ha-script-trace",load:()=>Promise.all([i.e(99528),i.e(74790),i.e(15101)]).then(i.bind(i,67876))}}})},{kind:"field",key:"_debouncedUpdateScripts",value(){return(0,a.D)((e=>{const t=this._getScripts(this.hass.states);D(t,e.scripts)||(e.scripts=t)}),10)}},{kind:"field",key:"_getScripts",value:()=>(0,o.Z)((e=>Object.values(e).filter((e=>"script"===(0,s.N)(e)))))},{kind:"method",key:"firstUpdated",value:function(e){x(z(r.prototype),"firstUpdated",this).call(this,e),this.hass.loadBackendTranslation("device_automation")}},{kind:"method",key:"updatePageEl",value:function(e,t){if(e.hass=this.hass,e.narrow=this.narrow,e.isWide=this.isWide,e.route=this.routeTail,e.showAdvanced=this.showAdvanced,this.hass&&(e.scripts&&t?t.has("hass")&&this._debouncedUpdateScripts(e):e.scripts=this._getScripts(this.hass.states)),(!t||t.has("route"))&&"dashboard"!==this._currentPage){e.creatingNew=void 0;const t=this.routeTail.path.substr(1);e.scriptEntityId="new"===t?null:t}}}]}}),l.n);r()}catch(S){r(S)}}))},67826:(e,t,i)=>{i.a(e,(async(e,t)=>{try{i(44577),i(53268),i(12730);var r=i(37500),n=i(36924),o=i(8636),s=i(14516),a=i(47181),l=i(27269),c=i(83849),d=i(83447),h=i(87744),p=i(50577),u=(i(81545),i(22098),i(36125),i(10983),i(52039),i(18900),i(44547)),f=i(26765),m=(i(27849),i(60010),i(23670)),y=i(11654),v=i(27322),g=i(81796),b=i(43547),k=i(19267),w=i(84407),_=e([k,w]);function E(e,t,i,r){var n=C();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(x(s.d.map(A)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function C(){C=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!P(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,M(t)||I(t)||H(t)||O()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=S(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:D(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=D(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function A(e){var t,i=S(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function $(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function x(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(z(o.descriptor)||z(n.descriptor)){if(P(o)||P(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(P(o)){if(P(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}$(o,n)}else t.push(o)}return t}function P(e){return e.decorators&&e.decorators.length}function z(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function D(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function S(e){var t=T(e,"string");return"symbol"==typeof t?t:String(t)}function T(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function O(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function H(e,t){if(e){if("string"==typeof e)return V(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?V(e,t):void 0}}function V(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function I(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function M(e){if(Array.isArray(e))return e}function j(){return j="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var r=F(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},j.apply(this,arguments)}function F(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=R(e)););return e}function R(e){return R=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},R(e)}[k,w]=_.then?(await _)():_;const B="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z",L="M11,17H4A2,2 0 0,1 2,15V3A2,2 0 0,1 4,1H16V3H4V15H11V13L15,16L11,19V17M19,21V7H8V13H6V7A2,2 0 0,1 8,5H19A2,2 0 0,1 21,7V21A2,2 0 0,1 19,23H8A2,2 0 0,1 6,21V19H8V21H19Z",Z="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z",U="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",q="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z",W="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z",Y="M8,5.14V19.14L19,12.14L8,5.14Z",N="M18 21L14 17H17V7H14L18 3L22 7H19V17H22M2 19V17H12V19M2 13V11H9V13M2 7V5H6V7H2Z",Q="M15,12C15,10.7 14.16,9.6 13,9.18V6.82C14.16,6.4 15,5.3 15,4A3,3 0 0,0 12,1A3,3 0 0,0 9,4C9,5.3 9.84,6.4 11,6.82V9.19C9.84,9.6 9,10.7 9,12C9,13.3 9.84,14.4 11,14.82V17.18C9.84,17.6 9,18.7 9,20A3,3 0 0,0 12,23A3,3 0 0,0 15,20C15,18.7 14.16,17.6 13,17.18V14.82C14.16,14.4 15,13.3 15,12M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M12,21A1,1 0 0,1 11,20A1,1 0 0,1 12,19A1,1 0 0,1 13,20A1,1 0 0,1 12,21Z";let K=E(null,(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"scriptEntityId",value:()=>null},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"route",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"isWide",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_entityId",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_idError",value:()=>!1},{kind:"field",decorators:[(0,n.SB)()],key:"_dirty",value:()=>!1},{kind:"field",decorators:[(0,n.SB)()],key:"_errors",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_mode",value:()=>"gui"},{kind:"field",decorators:[(0,n.IO)("ha-yaml-editor",!0)],key:"_yamlEditor",value:void 0},{kind:"field",decorators:[(0,n.IO)("manual-script-editor")],key:"_manualEditor",value:void 0},{kind:"field",key:"_schema",value(){return(0,s.Z)(((e,t,i)=>[{name:"alias",selector:{text:{type:"text"}}},{name:"icon",selector:{icon:{}}},...e?[]:[{name:"id",selector:{text:{}}}],...t?[]:[{name:"mode",selector:{select:{mode:"dropdown",options:u.EH.map((e=>({label:this.hass.localize(`ui.panel.config.script.editor.modes.${e}`),value:e})))}}}],...i&&(0,u.vA)(i)?[{name:"max",required:!0,selector:{number:{mode:"box",min:1,max:1/0}}}]:[]]))}},{kind:"method",key:"render",value:function(){var e;if(!this._config)return r.dy``;const t=this._schema(!!this.scriptEntityId,"use_blueprint"in this._config,this._config.mode),i={mode:u.EH[0],icon:void 0,max:this._config.mode&&(0,u.vA)(this._config.mode)?10:void 0,...this._config,id:this._entityId};return r.dy`
      <hass-subpage
        .hass=${this.hass}
        .narrow=${this.narrow}
        .route=${this.route}
        .backCallback=${this._backTapped}
        .header=${null!==(e=this._config)&&void 0!==e&&e.alias?this._config.alias:""}
      >
        ${this.scriptEntityId&&!this.narrow?r.dy`
              <mwc-button @click=${this._showTrace} slot="toolbar-icon">
                ${this.hass.localize("ui.panel.config.script.editor.show_trace")}
              </mwc-button>
            `:""}
        <ha-button-menu corner="BOTTOM_START" slot="toolbar-icon">
          <ha-icon-button
            slot="trigger"
            .label=${this.hass.localize("ui.common.menu")}
            .path=${q}
          ></ha-icon-button>

          <mwc-list-item
            graphic="icon"
            .disabled=${!this.scriptEntityId}
            @click=${this._showInfo}
          >
            ${this.hass.localize("ui.panel.config.script.editor.show_info")}
            <ha-svg-icon
              slot="graphic"
              .path=${W}
            ></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            graphic="icon"
            .disabled=${!this.scriptEntityId}
            @click=${this._runScript}
          >
            ${this.hass.localize("ui.panel.config.script.picker.run_script")}
            <ha-svg-icon slot="graphic" .path=${Y}></ha-svg-icon>
          </mwc-list-item>

          ${this.scriptEntityId&&this.narrow?r.dy`
                <a href="/config/script/trace/${this.scriptEntityId}">
                  <mwc-list-item graphic="icon">
                    ${this.hass.localize("ui.panel.config.script.editor.show_trace")}
                    <ha-svg-icon
                      slot="graphic"
                      .path=${Q}
                    ></ha-svg-icon>
                  </mwc-list-item>
                </a>
              `:""}
          ${this._config&&!("use_blueprint"in this._config)?r.dy`
                <mwc-list-item
                  aria-label=${this.hass.localize("ui.panel.config.automation.editor.re_order")}
                  graphic="icon"
                  .disabled=${"gui"!==this._mode}
                  @click=${this._toggleReOrderMode}
                >
                  ${this.hass.localize("ui.panel.config.automation.editor.re_order")}
                  <ha-svg-icon slot="graphic" .path=${N}></ha-svg-icon>
                </mwc-list-item>
              `:""}

          <li divider role="separator"></li>

          <mwc-list-item
            aria-label=${this.hass.localize("ui.panel.config.automation.editor.edit_ui")}
            graphic="icon"
            @click=${this._switchUiMode}
          >
            ${this.hass.localize("ui.panel.config.automation.editor.edit_ui")}
            ${"gui"===this._mode?r.dy`
                  <ha-svg-icon
                    class="selected_menu_item"
                    slot="graphic"
                    .path=${B}
                  ></ha-svg-icon>
                `:""}
          </mwc-list-item>
          <mwc-list-item
            aria-label=${this.hass.localize("ui.panel.config.automation.editor.edit_yaml")}
            graphic="icon"
            @click=${this._switchYamlMode}
          >
            ${this.hass.localize("ui.panel.config.automation.editor.edit_yaml")}
            ${"yaml"===this._mode?r.dy`
                  <ha-svg-icon
                    class="selected_menu_item"
                    slot="graphic"
                    .path=${B}
                  ></ha-svg-icon>
                `:""}
          </mwc-list-item>

          <li divider role="separator"></li>

          <mwc-list-item
            .disabled=${!this.scriptEntityId}
            .label=${this.hass.localize("ui.panel.config.script.picker.duplicate")}
            graphic="icon"
            @click=${this._duplicate}
          >
            ${this.hass.localize("ui.panel.config.script.picker.duplicate")}
            <ha-svg-icon
              slot="graphic"
              .path=${L}
            ></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            .disabled=${!this.scriptEntityId}
            aria-label=${this.hass.localize("ui.panel.config.script.picker.delete")}
            class=${(0,o.$)({warning:Boolean(this.scriptEntityId)})}
            graphic="icon"
            @click=${this._deleteConfirm}
          >
            ${this.hass.localize("ui.panel.config.script.picker.delete")}
            <ha-svg-icon
              class=${(0,o.$)({warning:Boolean(this.scriptEntityId)})}
              slot="graphic"
              .path=${U}
            >
            </ha-svg-icon>
          </mwc-list-item>
        </ha-button-menu>
        <div
          class="content ${(0,o.$)({"yaml-mode":"yaml"===this._mode})}"
        >
          ${this._errors?r.dy`<div class="errors">${this._errors}</div>`:""}
          ${"gui"===this._mode?r.dy`
                <div
                  class=${(0,o.$)({rtl:(0,h.HE)(this.hass)})}
                >
                  ${this._config?r.dy`
                        <div class="config-container">
                          <ha-card outlined>
                            <div class="card-content">
                              <ha-form
                                .schema=${t}
                                .data=${i}
                                .hass=${this.hass}
                                .computeLabel=${this._computeLabelCallback}
                                .computeHelper=${this._computeHelperCallback}
                                @value-changed=${this._valueChanged}
                              ></ha-form>
                            </div>
                          </ha-card>
                        </div>

                        ${"use_blueprint"in this._config?r.dy`
                              <blueprint-script-editor
                                .hass=${this.hass}
                                .narrow=${this.narrow}
                                .isWide=${this.isWide}
                                .config=${this._config}
                                @value-changed=${this._configChanged}
                              ></blueprint-script-editor>
                            `:r.dy`
                              <manual-script-editor
                                .hass=${this.hass}
                                .narrow=${this.narrow}
                                .isWide=${this.isWide}
                                .config=${this._config}
                                @value-changed=${this._configChanged}
                              ></manual-script-editor>
                            `}
                      `:""}
                </div>
              `:"yaml"===this._mode?r.dy`
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
        <ha-fab
          slot="fab"
          .label=${this.hass.localize("ui.panel.config.script.editor.save_script")}
          extended
          @click=${this._saveScript}
          class=${(0,o.$)({dirty:this._dirty})}
        >
          <ha-svg-icon slot="icon" .path=${Z}></ha-svg-icon>
        </ha-fab>
      </hass-subpage>
    `}},{kind:"method",key:"updated",value:function(e){j(R(i.prototype),"updated",this).call(this,e);const t=e.get("scriptEntityId");if(e.has("scriptEntityId")&&this.scriptEntityId&&this.hass&&(!t||t!==this.scriptEntityId)&&(0,u.Vn)(this.hass,(0,l.p)(this.scriptEntityId)).then((e=>{const t=e.sequence;t&&!Array.isArray(t)&&(e.sequence=[t]),this._dirty=!1,this._config=e}),(e=>{alert(404===e.status_code?this.hass.localize("ui.panel.config.script.editor.load_error_not_editable"):this.hass.localize("ui.panel.config.script.editor.load_error_unknown","err_no",e.status_code)),history.back()})),e.has("scriptEntityId")&&!this.scriptEntityId&&this.hass){const e=(0,u.FI)();this._dirty=!!e;const t={alias:this.hass.localize("ui.panel.config.script.editor.default_name")};e&&"use_blueprint"in e||(t.sequence=[{...b.x.defaultConfig}]),this._config={...t,...e}}}},{kind:"field",key:"_computeLabelCallback",value(){return(e,t)=>{switch(e.name){case"mode":return this.hass.localize("ui.panel.config.script.editor.modes.label");case"max":return this.hass.localize(`ui.panel.config.script.editor.max.${t.mode}`);default:return this.hass.localize(`ui.panel.config.script.editor.${e.name}`)}}}},{kind:"field",key:"_computeHelperCallback",value(){return e=>{if("mode"===e.name)return r.dy`
        <a
          style="color: var(--secondary-text-color)"
          href=${(0,v.R)(this.hass,"/integrations/script/#script-modes")}
          target="_blank"
          rel="noreferrer"
          >${this.hass.localize("ui.panel.config.script.editor.modes.learn_more")}</a
        >
      `}}},{kind:"method",key:"_showInfo",value:async function(){this.scriptEntityId&&(0,a.B)(this,"hass-more-info",{entityId:this.scriptEntityId})}},{kind:"method",key:"_showTrace",value:async function(){if(this.scriptEntityId){await this.confirmUnsavedChanged()&&(0,c.c)(`/config/script/trace/${this.scriptEntityId}`)}}},{kind:"method",key:"_runScript",value:async function(e){e.stopPropagation(),await(0,u.kC)(this.hass,this.scriptEntityId),(0,g.C)(this,{message:this.hass.localize("ui.notification_toast.triggered","name",this._config.alias)})}},{kind:"method",key:"_modeChanged",value:function(e){e!==(this._config.mode||u.EH[0])&&(this._config={...this._config,mode:e},(0,u.vA)(e)||delete this._config.max,this._dirty=!0)}},{kind:"method",key:"_aliasChanged",value:function(e){if(this.scriptEntityId||this._entityId&&this._entityId!==(0,d.l)(this._config.alias))return;const t=(0,d.l)(e);let i=t,r=2;for(;this.hass.states[`script.${i}`];)i=`${t}_${r}`,r++;this._entityId=i}},{kind:"method",key:"_idChanged",value:function(e){this._entityId=e,this.hass.states[`script.${this._entityId}`]?this._idError=!0:this._idError=!1}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation();const t=e.detail.value,i=this._entityId;let r=!1;for(const e of Object.keys(t)){if("sequence"===e)continue;const n=t[e];if(n!==this._config[e]&&("id"!==e||i!==n)){switch(r=!0,e){case"id":this._idChanged(n);break;case"alias":this._aliasChanged(n);break;case"mode":this._modeChanged(n)}if(void 0===t[e]){const t={...this._config};delete t[e],this._config=t}else this._config={...this._config,[e]:n}}}r&&(this._dirty=!0)}},{kind:"method",key:"_configChanged",value:function(e){this._config=e.detail.value,this._dirty=!0}},{kind:"method",key:"_preprocessYaml",value:function(){return this._config}},{kind:"method",key:"_copyYaml",value:async function(){var e;null!==(e=this._yamlEditor)&&void 0!==e&&e.yaml&&(await(0,p.v)(this._yamlEditor.yaml),(0,g.C)(this,{message:this.hass.localize("ui.common.copied_clipboard")}))}},{kind:"method",key:"_yamlChanged",value:function(e){e.stopPropagation(),e.detail.isValid&&(this._config=e.detail.value,this._errors=void 0,this._dirty=!0)}},{kind:"method",key:"confirmUnsavedChanged",value:async function(){return!this._dirty||(0,f.g7)(this,{text:this.hass.localize("ui.panel.config.automation.editor.unsaved_confirm"),confirmText:this.hass.localize("ui.common.leave"),dismissText:this.hass.localize("ui.common.stay")})}},{kind:"field",key:"_backTapped",value(){return async()=>{await this.confirmUnsavedChanged()&&history.back()}}},{kind:"method",key:"_duplicate",value:async function(){var e;await this.confirmUnsavedChanged()&&(0,u.rg)({...this._config,alias:`${null===(e=this._config)||void 0===e?void 0:e.alias} (${this.hass.localize("ui.panel.config.script.picker.duplicate")})`})}},{kind:"method",key:"_deleteConfirm",value:async function(){(0,f.g7)(this,{text:this.hass.localize("ui.panel.config.script.editor.delete_confirm"),confirmText:this.hass.localize("ui.common.delete"),dismissText:this.hass.localize("ui.common.cancel"),confirm:()=>this._delete()})}},{kind:"method",key:"_delete",value:async function(){await(0,u.oR)(this.hass,(0,l.p)(this.scriptEntityId)),history.back()}},{kind:"method",key:"_switchUiMode",value:function(){this._mode="gui"}},{kind:"method",key:"_switchYamlMode",value:function(){this._mode="yaml"}},{kind:"method",key:"_toggleReOrderMode",value:function(){this._manualEditor&&(this._manualEditor.reOrderMode=!this._manualEditor.reOrderMode)}},{kind:"method",key:"_saveScript",value:function(){if(this._idError)return void(0,g.C)(this,{message:this.hass.localize("ui.panel.config.script.editor.id_already_exists_save_error"),dismissable:!1,duration:0,action:{action:()=>{},text:this.hass.localize("ui.dialogs.generic.ok")}});const e=this.scriptEntityId?(0,l.p)(this.scriptEntityId):this._entityId||Date.now();this.hass.callApi("POST","config/script/config/"+e,this._config).then((()=>{this._dirty=!1,this.scriptEntityId||(0,c.c)(`/config/script/edit/${e}`,{replace:!0})}),(e=>{throw this._errors=e.body.message||e.error||e.body,(0,g.C)(this,{message:e.body.message||e.error||e.body}),e}))}},{kind:"method",key:"handleKeyboardSave",value:function(){this._saveScript()}},{kind:"get",static:!0,key:"styles",value:function(){return[y.Qx,r.iv`
        ha-card {
          overflow: hidden;
        }
        p {
          margin-bottom: 0;
        }
        .errors {
          padding: 20px;
          font-weight: bold;
          color: var(--error-color);
        }
        .yaml-mode {
          height: 100%;
          display: flex;
          flex-direction: column;
          padding-bottom: 0;
        }
        .config-container,
        manual-script-editor,
        blueprint-script-editor {
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
        span[slot="introduction"] a {
          color: var(--primary-color);
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
        .header {
          display: flex;
          margin: 16px 0;
          align-items: center;
        }
        .header .name {
          font-size: 20px;
          font-weight: 400;
          flex: 1;
        }
        .header a {
          color: var(--secondary-text-color);
        }
        ha-button-menu a {
          text-decoration: none;
          color: var(--primary-color);
        }
      `]}}]}}),(0,m.U)(r.oi));customElements.define("ha-script-editor",K),t()}catch(G){t(G)}}))},25931:(e,t,i)=>{i.a(e,(async(e,t)=>{try{var r=i(37500),n=i(36924),o=i(14516),s=i(44583),a=i(47181),l=i(27269),c=i(91741),d=i(83849),h=i(87744),p=(i(67556),i(36125),i(10983),i(48429),i(52039),i(44547)),u=i(26765),f=(i(96551),i(11654)),m=i(27322),y=i(81796),v=i(29311),g=e([s]);function b(e,t,i,r){var n=k();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(E(s.d.map(w)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function k(){k=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!C(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,O(t)||T(t)||D(t)||z()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=x(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:$(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=$(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function w(e){var t,i=x(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function _(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function E(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(A(o.descriptor)||A(n.descriptor)){if(C(o)||C(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(C(o)){if(C(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}_(o,n)}else t.push(o)}return t}function C(e){return e.decorators&&e.decorators.length}function A(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function $(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function x(e){var t=P(e,"string");return"symbol"==typeof t?t:String(t)}function P(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function z(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function D(e,t){if(e){if("string"==typeof e)return S(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?S(e,t):void 0}}function S(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function T(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function O(e){if(Array.isArray(e))return e}s=(g.then?(await g)():g)[0];const H="M11,17H4A2,2 0 0,1 2,15V3A2,2 0 0,1 4,1H16V3H4V15H11V13L15,16L11,19V17M19,21V7H8V13H6V7A2,2 0 0,1 8,5H19A2,2 0 0,1 21,7V21A2,2 0 0,1 19,23H8A2,2 0 0,1 6,21V19H8V21H19Z",V="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",I="M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z",M="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z",j="M8,5.14V19.14L19,12.14L8,5.14Z",F="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z",R="M15,12C15,10.7 14.16,9.6 13,9.18V6.82C14.16,6.4 15,5.3 15,4A3,3 0 0,0 12,1A3,3 0 0,0 9,4C9,5.3 9.84,6.4 11,6.82V9.19C9.84,9.6 9,10.7 9,12C9,13.3 9.84,14.4 11,14.82V17.18C9.84,17.6 9,18.7 9,20A3,3 0 0,0 12,23A3,3 0 0,0 15,20C15,18.7 14.16,17.6 13,17.18V14.82C14.16,14.4 15,13.3 15,12M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M12,21A1,1 0 0,1 11,20A1,1 0 0,1 12,19A1,1 0 0,1 13,20A1,1 0 0,1 12,21Z";b([(0,n.Mo)("ha-script-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"scripts",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"route",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"_activeFilters",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_filteredScripts",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_filterValue",value:void 0},{kind:"field",key:"_scripts",value:()=>(0,o.Z)(((e,t)=>null===t?[]:(t?e.filter((e=>t.includes(e.entity_id))):e).map((e=>({...e,name:(0,c.C)(e),last_triggered:e.attributes.last_triggered||void 0})))))},{kind:"field",key:"_columns",value(){return(0,o.Z)(((e,t)=>{const i={icon:{title:"",label:this.hass.localize("ui.panel.config.script.picker.headers.state"),type:"icon",template:(e,t)=>r.dy` <ha-state-icon .state=${t}></ha-state-icon>`},name:{title:this.hass.localize("ui.panel.config.script.picker.headers.name"),sortable:!0,filterable:!0,direction:"asc",grows:!0,template:e?(e,t)=>r.dy`
              ${e}
              <div class="secondary">
                ${this.hass.localize("ui.card.automation.last_triggered")}:
                ${t.attributes.last_triggered?(0,s.o0)(new Date(t.attributes.last_triggered),this.hass.locale):this.hass.localize("ui.components.relative_time.never")}
              </div>
            `:void 0}};return e||(i.last_triggered={sortable:!0,width:"40%",title:this.hass.localize("ui.card.automation.last_triggered"),template:e=>r.dy`
          ${e?(0,s.o0)(new Date(e),this.hass.locale):this.hass.localize("ui.components.relative_time.never")}
        `}),i.actions={title:"",width:this.narrow?void 0:"10%",type:"overflow-menu",template:(e,t)=>r.dy`
          <ha-icon-overflow-menu
            .hass=${this.hass}
            narrow
            .items=${[{path:M,label:this.hass.localize("ui.panel.config.script.picker.show_info"),action:()=>this._showInfo(t)},{path:j,label:this.hass.localize("ui.panel.config.script.picker.run"),action:()=>this._runScript(t)},{path:R,label:this.hass.localize("ui.panel.config.script.picker.show_trace"),action:()=>this._showTrace(t)},{divider:!0},{path:H,label:this.hass.localize("ui.panel.config.script.picker.duplicate"),action:()=>this._duplicate(t)},{label:this.hass.localize("ui.panel.config.script.picker.delete"),path:V,action:()=>this._deleteConfirm(t),warning:!0}]}
          >
          </ha-icon-overflow-menu>
        `},i}))}},{kind:"method",key:"render",value:function(){return r.dy`
      <hass-tabs-subpage-data-table
        .hass=${this.hass}
        .narrow=${this.narrow}
        back-path="/config"
        .route=${this.route}
        .tabs=${v.configSections.automations}
        .columns=${this._columns(this.narrow,this.hass.locale)}
        .data=${this._scripts(this.scripts,this._filteredScripts)}
        .activeFilters=${this._activeFilters}
        id="entity_id"
        .noDataText=${this.hass.localize("ui.panel.config.script.picker.no_scripts")}
        @clear-filter=${this._clearFilter}
        hasFab
        clickable
        @row-click=${this._handleRowClicked}
      >
        <ha-icon-button
          slot="toolbar-icon"
          .label=${this.hass.localize("ui.common.help")}
          .path=${I}
          @click=${this._showHelp}
        ></ha-icon-button>
        <ha-button-related-filter-menu
          slot="filter-menu"
          corner="BOTTOM_START"
          .narrow=${this.narrow}
          .hass=${this.hass}
          .value=${this._filterValue}
          exclude-domains='["script"]'
          @related-changed=${this._relatedFilterChanged}
        >
        </ha-button-related-filter-menu>
        <a href="/config/script/edit/new" slot="fab">
          <ha-fab
            ?is-wide=${this.isWide}
            ?narrow=${this.narrow}
            .label=${this.hass.localize("ui.panel.config.script.picker.add_script")}
            extended
            ?rtl=${(0,h.HE)(this.hass)}
          >
            <ha-svg-icon slot="icon" .path=${F}></ha-svg-icon>
          </ha-fab>
        </a>
      </hass-tabs-subpage-data-table>
    `}},{kind:"method",key:"_relatedFilterChanged",value:function(e){this._filterValue=e.detail.value,this._filterValue?(this._activeFilters=[e.detail.filter],this._filteredScripts=e.detail.items.script||null):this._clearFilter()}},{kind:"method",key:"_clearFilter",value:function(){this._filteredScripts=void 0,this._activeFilters=void 0,this._filterValue=void 0}},{kind:"method",key:"_handleRowClicked",value:function(e){(0,d.c)(`/config/script/edit/${e.detail.id}`)}},{kind:"field",key:"_runScript",value(){return async e=>{await(0,p.kC)(this.hass,e.entity_id),(0,y.C)(this,{message:this.hass.localize("ui.notification_toast.triggered","name",(0,c.C)(e))})}}},{kind:"method",key:"_showInfo",value:function(e){(0,a.B)(this,"hass-more-info",{entityId:e.entity_id})}},{kind:"method",key:"_showTrace",value:function(e){(0,d.c)(`/config/script/trace/${e.entity_id}`)}},{kind:"method",key:"_showHelp",value:function(){(0,u.Ys)(this,{title:this.hass.localize("ui.panel.config.script.caption"),text:r.dy`
        ${this.hass.localize("ui.panel.config.script.picker.introduction")}
        <p>
          <a
            href=${(0,m.R)(this.hass,"/docs/scripts/")}
            target="_blank"
            rel="noreferrer"
          >
            ${this.hass.localize("ui.panel.config.script.picker.learn_more")}
          </a>
        </p>
      `})}},{kind:"method",key:"_duplicate",value:async function(e){try{const t=await(0,p.Vn)(this.hass,(0,l.p)(e.entity_id));(0,p.rg)({...t,alias:`${null==t?void 0:t.alias} (${this.hass.localize("ui.panel.config.script.picker.duplicate")})`})}catch(e){await(0,u.Ys)(this,{text:404===e.status_code?this.hass.localize("ui.panel.config.script.editor.load_error_not_duplicable"):this.hass.localize("ui.panel.config.script.editor.load_error_unknown","err_no",e.status_code)})}}},{kind:"method",key:"_deleteConfirm",value:async function(e){(0,u.g7)(this,{text:this.hass.localize("ui.panel.config.script.editor.delete_confirm"),confirmText:this.hass.localize("ui.common.delete"),dismissText:this.hass.localize("ui.common.cancel"),confirm:()=>this._delete(e)})}},{kind:"method",key:"_delete",value:async function(e){try{await(0,p.oR)(this.hass,(0,l.p)(e.entity_id))}catch(e){await(0,u.Ys)(this,{text:400===e.status_code?this.hass.localize("ui.panel.config.script.editor.load_error_not_deletable"):this.hass.localize("ui.panel.config.script.editor.load_error_unknown","err_no",e.status_code)})}}},{kind:"get",static:!0,key:"styles",value:function(){return[f.Qx,r.iv`
        a {
          text-decoration: none;
        }
      `]}}]}}),r.oi);t()}catch(B){t(B)}}))},84407:(e,t,i)=>{i.a(e,(async(e,t)=>{try{i(51187);var r=i(37500),n=i(36924),o=i(47181),s=(i(9381),i(22098),i(10983),i(11654)),a=i(27322),l=i(61788),c=e([l]);function d(e,t,i,r){var n=h();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(f(s.d.map(p)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}function h(){h=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!m(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,C(t)||E(t)||w(t)||k()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=g(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:v(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=v(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function p(e){var t,i=g(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function u(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function f(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(y(o.descriptor)||y(n.descriptor)){if(m(o)||m(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(m(o)){if(m(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}u(o,n)}else t.push(o)}return t}function m(e){return e.decorators&&e.decorators.length}function y(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function v(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function g(e){var t=b(e,"string");return"symbol"==typeof t?t:String(t)}function b(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function k(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function w(e,t){if(e){if("string"==typeof e)return _(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?_(e,t):void 0}}function _(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function E(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function C(e){if(Array.isArray(e))return e}l=(c.then?(await c)():c)[0];const A="M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z";d([(0,n.Mo)("manual-script-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"config",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0,attribute:"re-order-mode"})],key:"reOrderMode",value:()=>!1},{kind:"method",key:"render",value:function(){return r.dy`
      ${this.reOrderMode?r.dy`
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

      <div class="header">
        <h2 id="sequence-heading" class="name">
          ${this.hass.localize("ui.panel.config.script.editor.sequence")}
        </h2>
        <a
          href=${(0,a.R)(this.hass,"/docs/scripts/")}
          target="_blank"
          rel="noreferrer"
        >
          <ha-icon-button
            .path=${A}
            .label=${this.hass.localize("ui.panel.config.script.editor.link_available_actions")}
          ></ha-icon-button>
        </a>
      </div>

      <ha-automation-action
        role="region"
        aria-labelledby="sequence-heading"
        .actions=${this.config.sequence}
        @value-changed=${this._sequenceChanged}
        .hass=${this.hass}
        .narrow=${this.narrow}
        .reOrderMode=${this.reOrderMode}
      ></ha-automation-action>
    `}},{kind:"method",key:"_sequenceChanged",value:function(e){e.stopPropagation(),(0,o.B)(this,"value-changed",{value:{...this.config,sequence:e.detail.value}})}},{kind:"method",key:"_exitReOrderMode",value:function(){this.reOrderMode=!this.reOrderMode}},{kind:"get",static:!0,key:"styles",value:function(){return[s.Qx,r.iv`
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
      `]}}]}}),r.oi);t()}catch($){t($)}}))}}]);
//# sourceMappingURL=845a29ef.js.map