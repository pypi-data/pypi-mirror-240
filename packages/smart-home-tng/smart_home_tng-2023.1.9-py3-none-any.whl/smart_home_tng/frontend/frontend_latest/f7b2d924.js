"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[38654],{38654:(e,t,i)=>{i.a(e,(async(e,n)=>{try{i.r(t);i(44577);var o=i(37500),r=i(33310),s=i(8636),a=i(14516),l=i(47181),d=i(58831),c=i(91741),u=i(45485),h=i(85415),p=i(65992),f=(i(81545),i(22098),i(83927),i(10983),i(43709),i(27434)),y=i(83270),m=i(74186),v=i(90363),g=(i(15291),i(60010),i(73826)),_=i(11654),k=e([p]);function x(e,t,i,n){var o=b();if(n)for(var r=0;r<n.length;r++)o=n[r](o);var s=t((function(e){o.initializeInstanceElements(e,a.elements)}),i),a=o.decorateClass(C(s.d.map(w)),e);return o.initializeClassElements(s.F,a.elements),o.runClassFinishers(s.F,a.finishers)}function b(){b=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var o=t.placement;if(t.kind===n&&("static"===o||"prototype"===o)){var r="static"===o?e:i;this.defineClassElement(r,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var n=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],n=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!S(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:i,finishers:n};var r=this.decorateConstructor(i,t);return n.push.apply(n,r.finishers),r.finishers=n,r},addElementPlacement:function(e,t,i){var n=t[e.placement];if(!i&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var i=[],n=[],o=e.decorators,r=o.length-1;r>=0;r--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[r])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&n.push(l.finisher);var d=l.extras;if(d){for(var c=0;c<d.length;c++)this.addElementPlacement(d[c],t);i.push.apply(i,d)}}return{element:e,finishers:n,extras:i}},decorateConstructor:function(e,t){for(var i=[],n=t.length-1;n>=0;n--){var o=this.fromClassDescriptor(e),r=this.toClassDescriptor((0,t[n])(o)||o);if(void 0!==r.finisher&&i.push(r.finisher),void 0!==r.elements){e=r.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,T(t)||M(t)||O(t)||P()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=A(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var r={kind:t,key:i,placement:n,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),r.initializer=e.initializer),r},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:L(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=L(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var n=(0,t[i])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function w(e){var t,i=A(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function E(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function C(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===r.key&&e.placement===r.placement},n=0;n<e.length;n++){var o,r=e[n];if("method"===r.kind&&(o=t.find(i)))if($(r.descriptor)||$(o.descriptor)){if(S(r)||S(o))throw new ReferenceError("Duplicated methods ("+r.key+") can't be decorated.");o.descriptor=r.descriptor}else{if(S(r)){if(S(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+r.key+").");o.decorators=r.decorators}E(r,o)}else t.push(r)}return t}function S(e){return e.decorators&&e.decorators.length}function $(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function L(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function A(e){var t=D(e,"string");return"symbol"==typeof t?t:String(t)}function D(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var n=i.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function P(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function O(e,t){if(e){if("string"==typeof e)return z(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?z(e,t):void 0}}function z(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,n=new Array(t);i<t;i++)n[i]=e[i];return n}function M(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function T(e){if(Array.isArray(e))return e}function j(){return j="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var n=H(e,t);if(n){var o=Object.getOwnPropertyDescriptor(n,t);return o.get?o.get.call(arguments.length<3?e:i):o.value}},j.apply(this,arguments)}function H(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=I(e)););return e}function I(e){return I=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},I(e)}p=(k.then?(await k)():k)[0];const V="M10,17L5,12L6.41,10.58L10,14.17L17.59,6.58L19,8M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z",F="M22,16A2,2 0 0,1 20,18H8C6.89,18 6,17.1 6,16V4C6,2.89 6.89,2 8,2H20A2,2 0 0,1 22,4V16M16,20V22H4A2,2 0 0,1 2,20V7H4V20H16M13,14L20,7L18.59,5.59L13,11.17L9.91,8.09L8.5,9.5L13,14Z",R="M19,3H16.3H7.7H5A2,2 0 0,0 3,5V7.7V16.4V19A2,2 0 0,0 5,21H7.7H16.4H19A2,2 0 0,0 21,19V16.3V7.7V5A2,2 0 0,0 19,3M15.6,17L12,13.4L8.4,17L7,15.6L10.6,12L7,8.4L8.4,7L12,10.6L15.6,7L17,8.4L13.4,12L17,15.6L15.6,17Z",B="M4 20H18V22H4C2.9 22 2 21.11 2 20V6H4V20M20.22 2H7.78C6.8 2 6 2.8 6 3.78V16.22C6 17.2 6.8 18 7.78 18H20.22C21.2 18 22 17.2 22 16.22V3.78C22 2.8 21.2 2 20.22 2M19 13.6L17.6 15L14 11.4L10.4 15L9 13.6L12.6 10L9 6.4L10.4 5L14 8.6L17.6 5L19 6.4L15.4 10L19 13.6Z",Z=!0,U=["Alexa.EndpointHealth"];x([(0,r.Mo)("cloud-alexa")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"cloudStatus",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_entities",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_entityConfigs",value:()=>({})},{kind:"field",decorators:[(0,r.SB)()],key:"_entityCategories",value:void 0},{kind:"field",key:"_popstateSyncAttached",value:()=>!1},{kind:"field",key:"_popstateReloadStatusAttached",value:()=>!1},{kind:"field",key:"_isInitialExposed",value:void 0},{kind:"field",key:"_getEntityFilterFunc",value:()=>(0,a.Z)((e=>(0,u.h)(e.include_domains,e.include_entities,e.exclude_domains,e.exclude_entities)))},{kind:"method",key:"render",value:function(){if(void 0===this._entities||void 0===this._entityCategories)return o.dy` <hass-loading-screen></hass-loading-screen> `;const e=(0,u.E)(this.cloudStatus.alexa_entities),t=this._getEntityFilterFunc(this.cloudStatus.alexa_entities),i=this._isInitialExposed||new Set,n=void 0===this._isInitialExposed;let r=0;const a=[],l=[];return this._entities.forEach((d=>{const c=this.hass.states[d.entity_id],u=this._entityConfigs[d.entity_id]||{should_expose:null},h=e?this._configIsExposed(d.entity_id,u,this._entityCategories[d.entity_id]):t(d.entity_id),p=e?this._configIsDomainExposed(d.entity_id,this._entityCategories[d.entity_id]):t(d.entity_id);h&&(r++,n&&i.add(d.entity_id));const f=i.has(d.entity_id)?a:l,y=o.dy`<ha-icon-button
        slot="trigger"
        class=${(0,s.$)({exposed:h,"not-exposed":!h})}
        .disabled=${!e}
        .label=${this.hass.localize("ui.panel.config.cloud.alexa.expose")}
        .path=${null!==u.should_expose?h?V:R:p?F:B}
      ></ha-icon-button>`;f.push(o.dy`
        <ha-card outlined>
          <div class="card-content">
            <div class="top-line">
              <state-info
                .hass=${this.hass}
                .stateObj=${c}
                secondary-line
                @click=${this._showMoreInfo}
              >
                ${d.interfaces.filter((e=>!U.includes(e))).map((e=>e.replace(/(Alexa.|Controller)/g,""))).join(", ")}
              </state-info>
              ${e?o.dy`<ha-button-menu
                    corner="BOTTOM_START"
                    .entityId=${c.entity_id}
                    @action=${this._exposeChanged}
                  >
                    ${y}
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.alexa.expose_entity")}
                      <ha-svg-icon
                        class="exposed"
                        slot="meta"
                        .path=${V}
                      ></ha-svg-icon>
                    </mwc-list-item>
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.alexa.dont_expose_entity")}
                      <ha-svg-icon
                        class="not-exposed"
                        slot="meta"
                        .path=${R}
                      ></ha-svg-icon>
                    </mwc-list-item>
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.alexa.follow_domain")}
                      <ha-svg-icon
                        class=${(0,s.$)({exposed:p,"not-exposed":!p})}
                        slot="meta"
                        .path=${p?F:B}
                      ></ha-svg-icon>
                    </mwc-list-item>
                  </ha-button-menu>`:o.dy`${y}`}
            </div>
          </div>
        </ha-card>
      `)})),n&&(this._isInitialExposed=i),o.dy`
      <hass-subpage .hass=${this.hass} .narrow=${this.narrow} .header=${this.hass.localize("ui.panel.config.cloud.alexa.title")}>
        ${e?o.dy`
                <mwc-button
                  slot="toolbar-icon"
                  @click=${this._openDomainToggler}
                  >${this.hass.localize("ui.panel.config.cloud.alexa.manage_defaults")}</mwc-button
                >
              `:""}
        ${e?"":o.dy`
                <div class="banner">
                  ${this.hass.localize("ui.panel.config.cloud.alexa.banner")}
                </div>
              `}
          ${a.length>0?o.dy`
                  <div class="header">
                    <h3>
                      ${this.hass.localize("ui.panel.config.cloud.alexa.exposed_entities")}
                    </h3>
                    ${this.narrow?r:this.hass.localize("ui.panel.config.cloud.alexa.exposed","selected",r)}
                  </div>
                  <div class="content">${a}</div>
                `:""}
          ${l.length>0?o.dy`
                  <div class="header second">
                    <h3>
                      ${this.hass.localize("ui.panel.config.cloud.alexa.not_exposed_entities")}
                    </h3>
                    ${this.narrow?this._entities.length-r:this.hass.localize("ui.panel.config.cloud.alexa.not_exposed","selected",this._entities.length-r)}
                  </div>
                  <div class="content">${l}</div>
                `:""}
        </div>
      </hass-subpage>
    `}},{kind:"method",key:"firstUpdated",value:function(e){j(I(i.prototype),"firstUpdated",this).call(this,e),this._fetchData()}},{kind:"method",key:"updated",value:function(e){j(I(i.prototype),"updated",this).call(this,e),e.has("cloudStatus")&&(this._entityConfigs=this.cloudStatus.prefs.alexa_entity_configs)}},{kind:"method",key:"hassSubscribe",value:function(){return[(0,m.LM)(this.hass.connection,(e=>{const t={};for(const i of e)t[i.entity_id]=i.entity_category;this._entityCategories=t}))]}},{kind:"method",key:"_fetchData",value:async function(){const e=await(0,f.t)(this.hass);e.sort(((e,t)=>{const i=this.hass.states[e.entity_id],n=this.hass.states[t.entity_id];return(0,h.$)(i?(0,c.C)(i):e.entity_id,n?(0,c.C)(n):t.entity_id)})),this._entities=e}},{kind:"method",key:"_showMoreInfo",value:function(e){const t=e.currentTarget.stateObj.entity_id;(0,l.B)(this,"hass-more-info",{entityId:t})}},{kind:"method",key:"_configIsDomainExposed",value:function(e,t){const i=(0,d.M)(e);return this.cloudStatus.prefs.alexa_default_expose?!t&&this.cloudStatus.prefs.alexa_default_expose.includes(i):Z}},{kind:"method",key:"_configIsExposed",value:function(e,t,i){var n;return null!==(n=t.should_expose)&&void 0!==n?n:this._configIsDomainExposed(e,i)}},{kind:"method",key:"_exposeChanged",value:async function(e){const t=e.currentTarget.entityId;let i=null;switch(e.detail.index){case 0:i=!0;break;case 1:i=!1;break;case 2:i=null}await this._updateExposed(t,i)}},{kind:"method",key:"_updateExposed",value:async function(e,t){await this._updateConfig(e,{should_expose:t}),this._ensureEntitySync()}},{kind:"method",key:"_updateConfig",value:async function(e,t){const i=await(0,y.tW)(this.hass,e,t);this._entityConfigs={...this._entityConfigs,[e]:i},this._ensureStatusReload()}},{kind:"method",key:"_openDomainToggler",value:function(){(0,v._)(this,{title:this.hass.localize("ui.panel.config.cloud.alexa.manage_defaults"),description:this.hass.localize("ui.panel.config.cloud.alexa.manage_defaults_dialog_description"),domains:this._entities.map((e=>(0,d.M)(e.entity_id))).filter(((e,t,i)=>i.indexOf(e)===t)),exposedDomains:this.cloudStatus.prefs.alexa_default_expose,toggleDomain:(e,t)=>{this._updateDomainExposed(e,t)},resetDomain:e=>{this._entities.forEach((t=>{(0,d.M)(t.entity_id)===e&&this._updateExposed(t.entity_id,null)}))}})}},{kind:"method",key:"_updateDomainExposed",value:async function(e,t){const i=this.cloudStatus.prefs.alexa_default_expose||this._entities.map((e=>(0,d.M)(e.entity_id))).filter(((e,t,i)=>i.indexOf(e)===t));t&&i.includes(e)||!t&&!i.includes(e)||(t?i.push(e):i.splice(i.indexOf(e),1),await(0,y.LV)(this.hass,{alexa_default_expose:i}),(0,l.B)(this,"ha-refresh-cloud-status"))}},{kind:"method",key:"_ensureStatusReload",value:function(){if(this._popstateReloadStatusAttached)return;this._popstateReloadStatusAttached=!0;const e=this.parentElement;window.addEventListener("popstate",(()=>(0,l.B)(e,"ha-refresh-cloud-status")),{once:!0})}},{kind:"method",key:"_ensureEntitySync",value:function(){this._popstateSyncAttached||(this._popstateSyncAttached=!0,window.addEventListener("popstate",(()=>{}),{once:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[_.Qx,o.iv`
        mwc-list-item > [slot="meta"] {
          margin-left: 4px;
        }
        .banner {
          color: var(--primary-text-color);
          background-color: var(
            --ha-card-background,
            var(--card-background-color, white)
          );
          padding: 16px 8px;
          text-align: center;
        }
        .content {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          grid-gap: 8px 8px;
          padding: 8px;
        }
        .card-content {
          padding-bottom: 12px;
        }
        state-info {
          cursor: pointer;
        }
        ha-switch {
          padding: 8px 0;
        }
        .top-line {
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
        .header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0 16px;
          border-bottom: 1px solid var(--divider-color);
          background: var(--app-header-background-color);
        }
        .header.second {
          border-top: 1px solid var(--divider-color);
        }
        .exposed {
          color: var(--success-color);
        }
        .not-exposed {
          color: var(--error-color);
        }
        @media all and (max-width: 450px) {
          ha-card {
            max-width: 100%;
          }
        }
      `]}}]}}),(0,g.f)(o.oi));n()}catch(N){n(N)}}))}}]);
//# sourceMappingURL=f7b2d924.js.map