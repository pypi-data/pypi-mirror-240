"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[19605],{31595:(e,t,r)=>{r.a(e,(async(e,t)=>{try{var i=r(37500),o=r(36924),n=r(63864),a=r(12198),s=r(44583),l=(r(32511),r(83927),r(33220),r(97712),e([a,s]));function c(e,t,r,i){var o=d();if(i)for(var n=0;n<i.length;n++)o=i[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),r),s=o.decorateClass(h(a.d.map(u)),e);return o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}function d(){d=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!f(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,P(t)||E(t)||g(t)||b()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=v(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:y(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=y(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function u(e){var t,r=v(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function h(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(m(n.descriptor)||m(o.descriptor)){if(f(n)||f(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(f(n)){if(f(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}p(n,o)}else t.push(n)}return t}function f(e){return e.decorators&&e.decorators.length}function m(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function y(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function v(e){var t=k(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function b(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function g(e,t){if(e){if("string"==typeof e)return w(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?w(e,t):void 0}}function w(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function E(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function P(e){if(Array.isArray(e))return e}function _(){return _="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var i=C(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(arguments.length<3?e:r):o.value}},_.apply(this,arguments)}function C(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=A(e)););return e}function A(e){return A=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},A(e)}[a,s]=l.then?(await l)():l;const $="M10,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V8C22,6.89 21.1,6 20,6H12L10,4Z",x="M21.8,13H20V21H13V17.67L15.79,14.88L16.5,15C17.66,15 18.6,14.06 18.6,12.9C18.6,11.74 17.66,10.8 16.5,10.8A2.1,2.1 0 0,0 14.4,12.9L14.5,13.61L13,15.13V9.65C13.66,9.29 14.1,8.6 14.1,7.8A2.1,2.1 0 0,0 12,5.7A2.1,2.1 0 0,0 9.9,7.8C9.9,8.6 10.34,9.29 11,9.65V15.13L9.5,13.61L9.6,12.9A2.1,2.1 0 0,0 7.5,10.8A2.1,2.1 0 0,0 5.4,12.9A2.1,2.1 0 0,0 7.5,15L8.21,14.88L11,17.67V21H4V13H2.25C1.83,13 1.42,13 1.42,12.79C1.43,12.57 1.85,12.15 2.28,11.72L11,3C11.33,2.67 11.67,2.33 12,2.33C12.33,2.33 12.67,2.67 13,3L17,7V6H19V9L21.78,11.78C22.18,12.18 22.59,12.59 22.6,12.8C22.6,13 22.2,13 21.8,13M7.5,12A0.9,0.9 0 0,1 8.4,12.9A0.9,0.9 0 0,1 7.5,13.8A0.9,0.9 0 0,1 6.6,12.9A0.9,0.9 0 0,1 7.5,12M16.5,12C17,12 17.4,12.4 17.4,12.9C17.4,13.4 17,13.8 16.5,13.8A0.9,0.9 0 0,1 15.6,12.9A0.9,0.9 0 0,1 16.5,12M12,6.9C12.5,6.9 12.9,7.3 12.9,7.8C12.9,8.3 12.5,8.7 12,8.7C11.5,8.7 11.1,8.3 11.1,7.8C11.1,7.3 11.5,6.9 12,6.9Z",T="M20.5,11H19V7C19,5.89 18.1,5 17,5H13V3.5A2.5,2.5 0 0,0 10.5,1A2.5,2.5 0 0,0 8,3.5V5H4A2,2 0 0,0 2,7V10.8H3.5C5,10.8 6.2,12 6.2,13.5C6.2,15 5,16.2 3.5,16.2H2V20A2,2 0 0,0 4,22H7.8V20.5C7.8,19 9,17.8 10.5,17.8C12,17.8 13.2,19 13.2,20.5V22H17A2,2 0 0,0 19,20V16H20.5A2.5,2.5 0 0,0 23,13.5A2.5,2.5 0 0,0 20.5,11Z",D=e=>{const t=[];return e.includes("ssl")&&t.push({slug:"ssl",name:"SSL",checked:!1}),e.includes("share")&&t.push({slug:"share",name:"Share",checked:!1}),e.includes("media")&&t.push({slug:"media",name:"Media",checked:!1}),e.includes("addons/local")&&t.push({slug:"addons/local",name:"Local add-ons",checked:!1}),t.sort(((e,t)=>e.name>t.name?1:-1))},S=e=>e.map((e=>({slug:e.slug,name:e.name,version:e.version,checked:!1}))).sort(((e,t)=>e.name>t.name?1:-1));c([(0,o.Mo)("supervisor-backup-content")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"localize",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"supervisor",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"backup",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"backupType",value:()=>"full"},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"folders",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"addons",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"homeAssistant",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"backupHasPassword",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"onboarding",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)()],key:"backupName",value:()=>""},{kind:"field",decorators:[(0,o.Cb)()],key:"backupPassword",value:()=>""},{kind:"field",decorators:[(0,o.Cb)()],key:"confirmBackupPassword",value:()=>""},{kind:"field",decorators:[(0,o.IO)("paper-input, ha-radio, ha-checkbox",!0)],key:"_focusTarget",value:void 0},{kind:"method",key:"willUpdate",value:function(e){var t,i,o,n;(_(A(r.prototype),"willUpdate",this).call(this,e),this.hasUpdated)||(this.folders=D(this.backup?this.backup.folders:["ssl","share","media","addons/local"]),this.addons=S(this.backup?this.backup.addons:null===(t=this.supervisor)||void 0===t?void 0:t.addon.addons),this.backupType=(null===(i=this.backup)||void 0===i?void 0:i.type)||"full",this.backupName=(null===(o=this.backup)||void 0===o?void 0:o.name)||"",this.backupHasPassword=(null===(n=this.backup)||void 0===n?void 0:n.protected)||!1)}},{kind:"method",key:"focus",value:function(){var e;null===(e=this._focusTarget)||void 0===e||e.focus()}},{kind:"field",key:"_localize",value(){return e=>{var t;return(null===(t=this.supervisor)||void 0===t?void 0:t.localize(`backup.${e}`))||this.localize(`ui.panel.page-onboarding.restore.${e}`)}}},{kind:"method",key:"render",value:function(){if(!this.onboarding&&!this.supervisor)return i.dy``;const e="partial"===this.backupType?this._getSection("folders"):void 0,t="partial"===this.backupType?this._getSection("addons"):void 0;return i.dy`
      ${this.backup?i.dy`<div class="details">
            ${"full"===this.backup.type?this._localize("full_backup"):this._localize("partial_backup")}
            (${Math.ceil(10*this.backup.size)/10+" MB"})<br />
            ${this.hass?(0,s.o0)(new Date(this.backup.date),this.hass.locale):this.backup.date}
          </div>`:i.dy`<paper-input
            name="backupName"
            .label=${this._localize("name")}
            .value=${this.backupName}
            @value-changed=${this._handleTextValueChanged}
          >
          </paper-input>`}
      ${this.backup&&"full"!==this.backup.type?"":i.dy`<div class="sub-header">
              ${this.backup?this._localize("select_type"):this._localize("type")}
            </div>
            <div class="backup-types">
              <ha-formfield .label=${this._localize("full_backup")}>
                <ha-radio
                  @change=${this._handleRadioValueChanged}
                  value="full"
                  name="backupType"
                  .checked=${"full"===this.backupType}
                >
                </ha-radio>
              </ha-formfield>
              <ha-formfield .label=${this._localize("partial_backup")}>
                <ha-radio
                  @change=${this._handleRadioValueChanged}
                  value="partial"
                  name="backupType"
                  .checked=${"partial"===this.backupType}
                >
                </ha-radio>
              </ha-formfield>
            </div>`}
      ${"partial"===this.backupType?i.dy`<div class="partial-picker">
            ${!this.backup||this.backup.homeassistant?i.dy`<ha-formfield
                  .label=${i.dy`<supervisor-formfield-label
                    label="Home Assistant"
                    .iconPath=${x}
                    .version=${this.backup?this.backup.homeassistant:this.hass.config.version}
                  >
                  </supervisor-formfield-label>`}
                >
                  <ha-checkbox
                    .checked=${this.homeAssistant}
                    @change=${this.toggleHomeAssistant}
                  >
                  </ha-checkbox>
                </ha-formfield>`:""}
            ${null!=e&&e.templates.length?i.dy`
                  <ha-formfield
                    .label=${i.dy`<supervisor-formfield-label
                      .label=${this._localize("folders")}
                      .iconPath=${$}
                    >
                    </supervisor-formfield-label>`}
                  >
                    <ha-checkbox
                      @change=${this._toggleSection}
                      .checked=${e.checked}
                      .indeterminate=${e.indeterminate}
                      .section=${"folders"}
                    >
                    </ha-checkbox>
                  </ha-formfield>
                  <div class="section-content">${e.templates}</div>
                `:""}
            ${null!=t&&t.templates.length?i.dy`
                  <ha-formfield
                    .label=${i.dy`<supervisor-formfield-label
                      .label=${this._localize("addons")}
                      .iconPath=${T}
                    >
                    </supervisor-formfield-label>`}
                  >
                    <ha-checkbox
                      @change=${this._toggleSection}
                      .checked=${t.checked}
                      .indeterminate=${t.indeterminate}
                      .section=${"addons"}
                    >
                    </ha-checkbox>
                  </ha-formfield>
                  <div class="section-content">${t.templates}</div>
                `:""}
          </div> `:""}
      ${"partial"!==this.backupType||this.backup&&!this.backupHasPassword?"":i.dy`<hr />`}
      ${this.backup?"":i.dy`<ha-formfield
            class="password"
            .label=${this._localize("password_protection")}
          >
            <ha-checkbox
              .checked=${this.backupHasPassword}
              @change=${this._toggleHasPassword}
            >
            </ha-checkbox>
          </ha-formfield>`}
      ${this.backupHasPassword?i.dy`
            <paper-input
              .label=${this._localize("password")}
              type="password"
              name="backupPassword"
              .value=${this.backupPassword}
              @value-changed=${this._handleTextValueChanged}
            >
            </paper-input>
            ${this.backup?"":i.dy` <paper-input
                  .label=${this._localize("confirm_password")}
                  type="password"
                  name="confirmBackupPassword"
                  .value=${this.confirmBackupPassword}
                  @value-changed=${this._handleTextValueChanged}
                >
                </paper-input>`}
          `:""}
    `}},{kind:"method",key:"toggleHomeAssistant",value:function(){this.homeAssistant=!this.homeAssistant}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      .partial-picker ha-formfield {
        display: block;
      }
      .partial-picker ha-checkbox {
        --mdc-checkbox-touch-target-size: 32px;
      }
      .partial-picker {
        display: block;
        margin: 0px -6px;
      }
      supervisor-formfield-label {
        display: inline-flex;
        align-items: center;
      }
      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }
      .details {
        color: var(--secondary-text-color);
      }
      .section-content {
        display: flex;
        flex-direction: column;
        margin-left: 30px;
      }
      ha-formfield.password {
        display: block;
        margin: 0 -14px -16px;
      }
      .backup-types {
        display: flex;
        margin-left: -13px;
      }
      .sub-header {
        margin-top: 8px;
      }
    `}},{kind:"method",key:"backupDetails",value:function(){var e,t;const r={};if(this.backup||(r.name=this.backupName||(0,a.p6)(new Date,this.hass.locale)),this.backupHasPassword&&(r.password=this.backupPassword,this.backup||(r.confirm_password=this.confirmBackupPassword)),"full"===this.backupType)return r;const i=null===(e=this.addons)||void 0===e?void 0:e.filter((e=>e.checked)).map((e=>e.slug)),o=null===(t=this.folders)||void 0===t?void 0:t.filter((e=>e.checked)).map((e=>e.slug));return null!=i&&i.length&&(r.addons=i),null!=o&&o.length&&(r.folders=o),r.homeassistant=this.homeAssistant,r}},{kind:"method",key:"_getSection",value:function(e){var t;const r=[],o="addons"===e?new Map(null===(t=this.supervisor)||void 0===t?void 0:t.addon.addons.map((e=>[e.slug,e]))):void 0;let a=0;this[e].forEach((t=>{var s;r.push(i.dy`<ha-formfield
        .label=${i.dy`<supervisor-formfield-label
          .label=${t.name}
          .iconPath=${"addons"===e?T:$}
          .imageUrl=${"addons"===e&&!this.onboarding&&(0,n.I)(this.hass.config.version,0,105)&&null!=o&&null!==(s=o.get(t.slug))&&void 0!==s&&s.icon?`/api/hassio/addons/${t.slug}/icon`:void 0}
          .version=${t.version}
        >
        </supervisor-formfield-label>`}
      >
        <ha-checkbox
          .item=${t}
          .checked=${t.checked}
          .section=${e}
          @change=${this._updateSectionEntry}
        >
        </ha-checkbox>
      </ha-formfield>`),t.checked&&a++}));const s=a===this[e].length;return{templates:r,checked:s,indeterminate:!s&&0!==a}}},{kind:"method",key:"_handleRadioValueChanged",value:function(e){const t=e.currentTarget;this[t.name]=t.value}},{kind:"method",key:"_handleTextValueChanged",value:function(e){this[e.currentTarget.name]=e.detail.value}},{kind:"method",key:"_toggleHasPassword",value:function(){this.backupHasPassword=!this.backupHasPassword}},{kind:"method",key:"_toggleSection",value:function(e){const t=e.currentTarget.section;this[t]=("addons"===t?this.addons:this.folders).map((t=>({...t,checked:e.currentTarget.checked})))}},{kind:"method",key:"_updateSectionEntry",value:function(e){const t=e.currentTarget.item,r=e.currentTarget.section;this[r]=this[r].map((r=>r.slug===t.slug?{...r,checked:e.currentTarget.checked}:r))}}]}}),i.oi);t()}catch(z){t(z)}}))},97712:(e,t,r)=>{var i=r(37500),o=r(36924);r(52039);function n(){n=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!l(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function a(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function s(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function l(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var o=n();if(i)for(var d=0;d<i.length;d++)o=i[d](o);var u=t((function(e){o.initializeInstanceElements(e,p.elements)}),r),p=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(c(n.descriptor)||c(o.descriptor)){if(l(n)||l(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(l(n)){if(l(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}s(n,o)}else t.push(n)}return t}(u.d.map(a)),e);o.initializeClassElements(u.F,p.elements),o.runClassFinishers(u.F,p.finishers)}([(0,o.Mo)("supervisor-formfield-label")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({type:String})],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:String})],key:"imageUrl",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:String})],key:"iconPath",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:String})],key:"version",value:void 0},{kind:"method",key:"render",value:function(){return i.dy`
      ${this.imageUrl?i.dy`<img loading="lazy" .src=${this.imageUrl} class="icon" />`:this.iconPath?i.dy`<ha-svg-icon .path=${this.iconPath} class="icon"></ha-svg-icon>`:""}
      <span class="label">${this.label}</span>
      ${this.version?i.dy`<span class="version">(${this.version})</span>`:""}
    `}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        display: flex;
        align-items: center;
      }
      .label {
        margin-right: 4px;
      }
      .version {
        color: var(--secondary-text-color);
      }
      .icon {
        max-height: 22px;
        max-width: 22px;
        margin-right: 8px;
      }
    `}}]}}),i.oi)},19605:(e,t,r)=>{r.a(e,(async(e,i)=>{try{r.r(t);r(44577);var o=r(37500),n=r(36924),a=r(47181),s=r(83447),l=(r(98762),r(9381),r(81545),r(90806),r(10983),r(22814)),c=r(41682),d=r(60538),u=r(26765),p=r(11654),h=r(25936),f=r(31595),m=r(63864),y=r(32594),v=e([f]);function k(e,t,r,i){var o=b();if(i)for(var n=0;n<i.length;n++)o=i[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),r),s=o.decorateClass(E(a.d.map(g)),e);return o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}function b(){b=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!P(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,z(t)||S(t)||T(t)||x()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=A(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:C(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=C(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function g(e){var t,r=A(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function w(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function E(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(_(n.descriptor)||_(o.descriptor)){if(P(n)||P(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(P(n)){if(P(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}w(n,o)}else t.push(n)}return t}function P(e){return e.decorators&&e.decorators.length}function _(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function C(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function A(e){var t=$(e,"string");return"symbol"==typeof t?t:String(t)}function $(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function x(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function T(e,t){if(e){if("string"==typeof e)return D(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?D(e,t):void 0}}function D(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function S(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function z(e){if(Array.isArray(e))return e}f=(v.then?(await v)():v)[0];const O="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",L="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z";k([(0,n.Mo)("dialog-hassio-backup")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_backup",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_dialogParams",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_restoringBackup",value:()=>!1},{kind:"field",decorators:[(0,n.IO)("supervisor-backup-content")],key:"_backupContent",value:void 0},{kind:"method",key:"showDialog",value:async function(e){this._backup=await(0,d._P)(this.hass,e.slug),this._dialogParams=e,this._restoringBackup=!1}},{kind:"method",key:"closeDialog",value:function(){this._backup=void 0,this._dialogParams=void 0,this._restoringBackup=!1,this._error=void 0,(0,a.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var e,t,r;return this._dialogParams&&this._backup?o.dy`
      <ha-dialog
        open
        scrimClickAction
        @closed=${this.closeDialog}
        .heading=${this._backup.name}
      >
        <div slot="heading">
          <ha-header-bar>
            <span slot="title">${this._backup.name}</span>
            <ha-icon-button
              .label=${(null===(e=this.hass)||void 0===e?void 0:e.localize("ui.common.close"))||"Close"}
              .path=${O}
              slot="actionItems"
              dialogAction="cancel"
            ></ha-icon-button>
          </ha-header-bar>
        </div>
        ${this._restoringBackup?o.dy` <ha-circular-progress active></ha-circular-progress>`:o.dy`<supervisor-backup-content
              .hass=${this.hass}
              .supervisor=${this._dialogParams.supervisor}
              .backup=${this._backup}
              .onboarding=${this._dialogParams.onboarding||!1}
              .localize=${this._dialogParams.localize}
              dialogInitialFocus
            >
            </supervisor-backup-content>`}
        ${this._error?o.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}

        <mwc-button
          .disabled=${this._restoringBackup}
          slot="secondaryAction"
          @click=${this._restoreClicked}
        >
          Restore
        </mwc-button>

        ${this._dialogParams.onboarding?"":o.dy`<ha-button-menu
              fixed
              slot="primaryAction"
              @action=${this._handleMenuAction}
              @closed=${y.U}
            >
              <ha-icon-button
                .label=${this.hass.localize("ui.common.menu")||"Menu"}
                .path=${L}
                slot="trigger"
              ></ha-icon-button>
              <mwc-list-item
                >${null===(t=this._dialogParams.supervisor)||void 0===t?void 0:t.localize("backup.download_backup")}</mwc-list-item
              >
              <mwc-list-item class="error"
                >${null===(r=this._dialogParams.supervisor)||void 0===r?void 0:r.localize("backup.delete_backup_title")}</mwc-list-item
              >
            </ha-button-menu>`}
      </ha-dialog>
    `:o.dy``}},{kind:"get",static:!0,key:"styles",value:function(){return[p.Qx,p.yu,o.iv`
        ha-circular-progress {
          display: block;
          text-align: center;
        }
        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
          display: block;
        }
        ha-icon-button {
          color: var(--secondary-text-color);
        }
      `]}},{kind:"method",key:"_handleMenuAction",value:function(e){switch(e.detail.index){case 0:this._downloadClicked();break;case 1:this._deleteClicked()}}},{kind:"method",key:"_restoreClicked",value:async function(){const e=this._backupContent.backupDetails();this._restoringBackup=!0,"full"===this._backupContent.backupType?await this._fullRestoreClicked(e):await this._partialRestoreClicked(e),this._restoringBackup=!1}},{kind:"method",key:"_partialRestoreClicked",value:async function(e){var t,r,i,o;if(void 0===(null===(t=this._dialogParams)||void 0===t?void 0:t.supervisor)||"running"===(null===(r=this._dialogParams)||void 0===r?void 0:r.supervisor.info.state)){if(await(0,u.g7)(this,{title:"Are you sure you want partially to restore this backup?",confirmText:"restore",dismissText:"cancel"}))if(null!==(i=this._dialogParams)&&void 0!==i&&i.onboarding)(0,a.B)(this,"restoring"),await fetch(`/api/hassio/backups/${this._backup.slug}/restore/partial`,{method:"POST",body:JSON.stringify(e)}),this.closeDialog();else try{await this.hass.callApi("POST",`hassio/${(0,m.I)(this.hass.config.version,2021,9)?"backups":"snapshots"}/${this._backup.slug}/restore/partial`,e),this.closeDialog()}catch(e){this._error=e.body.message}}else await(0,u.Ys)(this,{title:"Could not restore backup",text:`Restoring a backup is not possible right now because the system is in ${null===(o=this._dialogParams)||void 0===o?void 0:o.supervisor.info.state} state.`})}},{kind:"method",key:"_fullRestoreClicked",value:async function(e){var t,r,i,o;void 0===(null===(t=this._dialogParams)||void 0===t?void 0:t.supervisor)||"running"===(null===(r=this._dialogParams)||void 0===r?void 0:r.supervisor.info.state)?await(0,u.g7)(this,{title:"Are you sure you want to wipe your system and restore this backup?",confirmText:"restore",dismissText:"cancel"})&&(null!==(i=this._dialogParams)&&void 0!==i&&i.onboarding?((0,a.B)(this,"restoring"),fetch(`/api/hassio/backups/${this._backup.slug}/restore/full`,{method:"POST",body:JSON.stringify(e)}),this.closeDialog()):this.hass.callApi("POST",`hassio/${(0,m.I)(this.hass.config.version,2021,9)?"backups":"snapshots"}/${this._backup.slug}/restore/full`,e).then((()=>{this.closeDialog()}),(e=>{this._error=e.body.message}))):await(0,u.Ys)(this,{title:"Could not restore backup",text:`Restoring a backup is not possible right now because the system is in ${null===(o=this._dialogParams)||void 0===o?void 0:o.supervisor.info.state} state.`})}},{kind:"method",key:"_deleteClicked",value:async function(){await(0,u.g7)(this,{title:"Are you sure you want to delete this backup?",confirmText:"delete",dismissText:"cancel"})&&this.hass.callApi((0,m.I)(this.hass.config.version,2021,9)?"DELETE":"POST","hassio/"+((0,m.I)(this.hass.config.version,2021,9)?`backups/${this._backup.slug}`:`snapshots/${this._backup.slug}/remove`)).then((()=>{this._dialogParams.onDelete&&this._dialogParams.onDelete(),this.closeDialog()}),(e=>{this._error=e.body.message}))}},{kind:"method",key:"_downloadClicked",value:async function(){let e;try{e=await(0,l.iI)(this.hass,`/api/hassio/${(0,m.I)(this.hass.config.version,2021,9)?"backups":"snapshots"}/${this._backup.slug}/download`)}catch(e){return void await(0,u.Ys)(this,{text:(0,c.js)(e)})}if(window.location.href.includes("ui.nabu.casa")){if(!await(0,u.g7)(this,{title:"Potential slow download",text:"Downloading backups over the Nabu Casa URL will take some time, it is recommended to use your local URL instead, do you want to continue?",confirmText:"continue",dismissText:"cancel"}))return}(0,h.N)(e.path,`home_assistant_backup_${(0,s.l)(this._computeName)}.tar`)}},{kind:"get",key:"_computeName",value:function(){return this._backup?this._backup.name||this._backup.slug:"Unnamed backup"}}]}}),o.oi);i()}catch(F){i(F)}}))},12198:(e,t,r)=>{r.a(e,(async(e,i)=>{try{r.d(t,{D_:()=>e,NC:()=>h,Nh:()=>m,WB:()=>c,mn:()=>u,p6:()=>s,yQ:()=>v});var o=r(14516),n=r(92874);n.Xp&&await n.Xp;const e=(e,t)=>a(t).format(e),a=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{weekday:"long",month:"long",day:"numeric"}))),s=(e,t)=>l(t).format(e),l=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{year:"numeric",month:"long",day:"numeric"}))),c=(e,t)=>d(t).format(e),d=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{year:"numeric",month:"numeric",day:"numeric"}))),u=(e,t)=>p(t).format(e),p=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{day:"numeric",month:"short"}))),h=(e,t)=>f(t).format(e),f=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{month:"long",year:"numeric"}))),m=(e,t)=>y(t).format(e),y=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{month:"long"}))),v=(e,t)=>k(t).format(e),k=(0,o.Z)((e=>new Intl.DateTimeFormat(e.language,{year:"numeric"})));i()}catch(e){i(e)}}),1)},44583:(e,t,r)=>{r.a(e,(async(e,i)=>{try{r.d(t,{E8:()=>l,o0:()=>e});var o=r(14516),n=r(92874),a=r(65810);n.Xp&&await n.Xp;const e=(e,t)=>s(t).format(e),s=(0,o.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,a.y)(e)?e.language:"en-u-hc-h23",{year:"numeric",month:"long",day:"numeric",hour:(0,a.y)(e)?"numeric":"2-digit",minute:"2-digit",hour12:(0,a.y)(e)}))),l=((0,o.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,a.y)(e)?e.language:"en-u-hc-h23",{month:"short",day:"numeric",hour:(0,a.y)(e)?"numeric":"2-digit",minute:"2-digit",hour12:(0,a.y)(e)}))),(e,t)=>c(t).format(e)),c=(0,o.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,a.y)(e)?e.language:"en-u-hc-h23",{year:"numeric",month:"long",day:"numeric",hour:(0,a.y)(e)?"numeric":"2-digit",minute:"2-digit",second:"2-digit",hour12:(0,a.y)(e)})));(0,o.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,a.y)(e)?e.language:"en-u-hc-h23",{year:"numeric",month:"numeric",day:"numeric",hour:"numeric",minute:"2-digit",hour12:(0,a.y)(e)})));i()}catch(e){i(e)}}),1)},65810:(e,t,r)=>{r.d(t,{y:()=>n});var i=r(14516),o=r(66477);const n=(0,i.Z)((e=>{if(e.time_format===o.zt.language||e.time_format===o.zt.system){const t=e.time_format===o.zt.language?e.language:void 0,r=(new Date).toLocaleString(t);return r.includes("AM")||r.includes("PM")}return e.time_format===o.zt.am_pm}))},83447:(e,t,r)=>{r.d(t,{l:()=>i});const i=(e,t="_")=>{const r="àáäâãåăæąçćčđďèéěėëêęğǵḧìíïîįłḿǹńňñòóöôœøṕŕřßşśšșťțùúüûǘůűūųẃẍÿýźžż·/_,:;",i=`aaaaaaaaacccddeeeeeeegghiiiiilmnnnnooooooprrsssssttuuuuuuuuuwxyyzzz${t}${t}${t}${t}${t}${t}`,o=new RegExp(r.split("").join("|"),"g");return e.toString().toLowerCase().replace(/\s+/g,t).replace(o,(e=>i.charAt(r.indexOf(e)))).replace(/&/g,`${t}and${t}`).replace(/[^\w-]+/g,"").replace(/-/g,t).replace(new RegExp(`(${t})\\1+`,"g"),"$1").replace(new RegExp(`^${t}+`),"").replace(new RegExp(`${t}+$`),"")}},98762:(e,t,r)=>{r(51187);var i=r(37500),o=r(36924);r(31206),r(52039);function n(){n=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!l(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[n])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function a(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function s(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function l(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var o=n();if(i)for(var d=0;d<i.length;d++)o=i[d](o);var u=t((function(e){o.initializeInstanceElements(e,p.elements)}),r),p=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(c(n.descriptor)||c(o.descriptor)){if(l(n)||l(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(l(n)){if(l(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}s(n,o)}else t.push(n)}return t}(u.d.map(a)),e);o.initializeClassElements(u.F,p.elements),o.runClassFinishers(u.F,p.finishers)}([(0,o.Mo)("ha-progress-button")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"progress",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"raised",value:()=>!1},{kind:"field",decorators:[(0,o.SB)()],key:"_result",value:void 0},{kind:"method",key:"render",value:function(){const e=this._result||this.progress;return i.dy`
      <mwc-button
        ?raised=${this.raised}
        .disabled=${this.disabled||this.progress}
        @click=${this._buttonTapped}
        class=${this._result||""}
      >
        <slot></slot>
      </mwc-button>
      ${e?i.dy`
            <div class="progress">
              ${"success"===this._result?i.dy`<ha-svg-icon .path=${"M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z"}></ha-svg-icon>`:"error"===this._result?i.dy`<ha-svg-icon .path=${"M2.2,16.06L3.88,12L2.2,7.94L6.26,6.26L7.94,2.2L12,3.88L16.06,2.2L17.74,6.26L21.8,7.94L20.12,12L21.8,16.06L17.74,17.74L16.06,21.8L12,20.12L7.94,21.8L6.26,17.74L2.2,16.06M13,17V15H11V17H13M13,13V7H11V13H13Z"}></ha-svg-icon>`:this.progress?i.dy`
                    <ha-circular-progress
                      size="small"
                      active
                    ></ha-circular-progress>
                  `:""}
            </div>
          `:""}
    `}},{kind:"method",key:"actionSuccess",value:function(){this._setResult("success")}},{kind:"method",key:"actionError",value:function(){this._setResult("error")}},{kind:"method",key:"_setResult",value:function(e){this._result=e,setTimeout((()=>{this._result=void 0}),2e3)}},{kind:"method",key:"_buttonTapped",value:function(e){this.progress&&e.stopPropagation()}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        outline: none;
        display: inline-block;
        position: relative;
      }

      mwc-button {
        transition: all 1s;
      }

      mwc-button.success {
        --mdc-theme-primary: white;
        background-color: var(--success-color);
        transition: none;
        border-radius: 4px;
        pointer-events: none;
      }

      mwc-button[raised].success {
        --mdc-theme-primary: var(--success-color);
        --mdc-theme-on-primary: white;
      }

      mwc-button.error {
        --mdc-theme-primary: white;
        background-color: var(--error-color);
        transition: none;
        border-radius: 4px;
        pointer-events: none;
      }

      mwc-button[raised].error {
        --mdc-theme-primary: var(--error-color);
        --mdc-theme-on-primary: white;
      }

      .progress {
        bottom: 4px;
        position: absolute;
        text-align: center;
        top: 4px;
        width: 100%;
      }

      ha-svg-icon {
        color: white;
      }

      mwc-button.success slot,
      mwc-button.error slot {
        visibility: hidden;
      }
    `}}]}}),i.oi)},25936:(e,t,r)=>{r.d(t,{N:()=>i});const i=(e,t="")=>{const r=document.createElement("a");r.target="_blank",r.href=e,r.download=t,document.body.appendChild(r),r.dispatchEvent(new MouseEvent("click")),document.body.removeChild(r)}}}]);
//# sourceMappingURL=5cdca862.js.map