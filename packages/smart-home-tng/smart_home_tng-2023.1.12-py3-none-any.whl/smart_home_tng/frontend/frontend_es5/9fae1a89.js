/*! For license information please see 9fae1a89.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[88906],{18601:function(e,t,r){r.d(t,{Wg:function(){return l},qN:function(){return a.q}});var i,n,o=r(43204),s=r(36924),a=r(78220);const c=null!==(n=null===(i=window.ShadyDOM)||void 0===i?void 0:i.inUse)&&void 0!==n&&n;class l extends a.H{constructor(){super(...arguments),this.disabled=!1,this.containingForm=null,this.formDataListener=e=>{this.disabled||this.setFormData(e.formData)}}findFormElement(){if(!this.shadowRoot||c)return null;const e=this.getRootNode().querySelectorAll("form");for(const t of Array.from(e))if(t.contains(this))return t;return null}connectedCallback(){var e;super.connectedCallback(),this.containingForm=this.findFormElement(),null===(e=this.containingForm)||void 0===e||e.addEventListener("formdata",this.formDataListener)}disconnectedCallback(){var e;super.disconnectedCallback(),null===(e=this.containingForm)||void 0===e||e.removeEventListener("formdata",this.formDataListener),this.containingForm=null}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(e=>{this.dispatchEvent(new Event("change",e))}))}}l.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,o.__decorate)([(0,s.Cb)({type:Boolean})],l.prototype,"disabled",void 0)},14114:function(e,t,r){r.d(t,{P:function(){return i}});const i=e=>(t,r)=>{if(t.constructor._observers){if(!t.constructor.hasOwnProperty("_observers")){const e=t.constructor._observers;t.constructor._observers=new Map,e.forEach(((e,r)=>t.constructor._observers.set(r,e)))}}else{t.constructor._observers=new Map;const e=t.updated;t.updated=function(t){e.call(this,t),t.forEach(((e,t)=>{const r=this.constructor._observers.get(t);void 0!==r&&r.call(this,this[t],e)}))}}t.constructor._observers.set(r,e)}},3239:function(e,t,r){function i(e){if(!e||"object"!=typeof e)return e;if("[object Date]"==Object.prototype.toString.call(e))return new Date(e.getTime());if(Array.isArray(e))return e.map(i);var t={};return Object.keys(e).forEach((function(r){t[r]=i(e[r])})),t}r.d(t,{Z:function(){return i}})},80033:function(e,t,r){r.d(t,{Dm:function(){return a},jg:function(){return o},p4:function(){return n},pN:function(){return s},xC:function(){return i}});const i=e=>{let t=e;return"string"==typeof e&&(t=parseInt(e,16)),"0x"+t.toString(16).padStart(4,"0")},n=e=>e.split(":").slice(-4).reverse().join(""),o=(e,t)=>{const r=e.user_given_name?e.user_given_name:e.name,i=t.user_given_name?t.user_given_name:t.name;return r.localeCompare(i)},s=(e,t)=>{const r=e.name,i=t.name;return r.localeCompare(i)},a=e=>`${e.name} (Endpoint id: ${e.endpoint_id}, Id: ${i(e.id)}, Type: ${e.type})`},86444:function(e,t,r){r.r(t),r.d(t,{ZHAGroupPage:function(){return y}});r(51187);var i=r(37500),n=r(36924),o=r(83849),s=(r(31206),r(10983),r(22383)),a=(r(48811),r(60010),r(88165),r(80033));r(79484);function c(){c=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!u(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,n[o])(a)||a);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return m(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?m(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=f(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function l(e){var t,r=f(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function d(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function u(e){return e.decorators&&e.decorators.length}function p(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function f(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function v(){return v="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=g(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(arguments.length<3?e:r):n.value}},v.apply(this,arguments)}function g(e){return g=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},g(e)}let y=function(e,t,r,i){var n=c();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var s=t((function(e){n.initializeInstanceElements(e,a.elements)}),r),a=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(p(o.descriptor)||p(n.descriptor)){if(u(o)||u(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(u(o)){if(u(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}d(o,n)}else t.push(o)}return t}(s.d.map(l)),e);return n.initializeClassElements(s.F,a.elements),n.runClassFinishers(s.F,a.finishers)}([(0,n.Mo)("zha-group-page")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,n.Cb)({type:Object})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Object})],key:"group",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Number})],key:"groupId",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array})],key:"deviceEndpoints",value(){return[]}},{kind:"field",decorators:[(0,n.SB)()],key:"_processingAdd",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_processingRemove",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_filteredDeviceEndpoints",value(){return[]}},{kind:"field",decorators:[(0,n.SB)()],key:"_selectedDevicesToAdd",value(){return[]}},{kind:"field",decorators:[(0,n.SB)()],key:"_selectedDevicesToRemove",value(){return[]}},{kind:"field",decorators:[(0,n.IO)("#addMembers",!0)],key:"_zhaAddMembersDataTable",value:void 0},{kind:"field",decorators:[(0,n.IO)("#removeMembers")],key:"_zhaRemoveMembersDataTable",value:void 0},{kind:"field",key:"_firstUpdatedCalled",value(){return!1}},{kind:"method",key:"connectedCallback",value:function(){v(g(r.prototype),"connectedCallback",this).call(this),this.hass&&this._firstUpdatedCalled&&this._fetchData()}},{kind:"method",key:"disconnectedCallback",value:function(){v(g(r.prototype),"disconnectedCallback",this).call(this),this._processingAdd=!1,this._processingRemove=!1,this._selectedDevicesToRemove=[],this._selectedDevicesToAdd=[],this.deviceEndpoints=[],this._filteredDeviceEndpoints=[]}},{kind:"method",key:"firstUpdated",value:function(e){v(g(r.prototype),"firstUpdated",this).call(this,e),this.hass&&this._fetchData(),this._firstUpdatedCalled=!0}},{kind:"method",key:"render",value:function(){return this.group?i.dy`
      <hass-subpage
        .hass=${this.hass}
        .narrow=${this.narrow}
        .header=${this.group.name}
      >
        <ha-icon-button
          slot="toolbar-icon"
          .path=${"M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"}
          @click=${this._deleteGroup}
          .label=${this.hass.localize("ui.panel.config.zha.groups.delete")}
        ></ha-icon-button>
        <ha-config-section .isWide=${this.isWide}>
          <div class="header">
            ${this.hass.localize("ui.panel.config.zha.groups.group_info")}
          </div>

          <p slot="introduction">
            ${this.hass.localize("ui.panel.config.zha.groups.group_details")}
          </p>

          <p><b>Name:</b> ${this.group.name}</p>
          <p><b>Group Id:</b> ${(0,a.xC)(this.group.group_id)}</p>

          <div class="header">
            ${this.hass.localize("ui.panel.config.zha.groups.members")}
          </div>
          <ha-card>
            ${this.group.members.length?this.group.members.map((e=>i.dy`<a
                      href="/config/devices/device/${e.device.device_reg_id}"
                    >
                      <paper-item
                        >${e.device.user_given_name||e.device.name}</paper-item
                      >
                    </a>`)):i.dy` <paper-item> This group has no members </paper-item> `}
          </ha-card>
          ${this.group.members.length?i.dy`
                <div class="header">
                  ${this.hass.localize("ui.panel.config.zha.groups.remove_members")}
                </div>

                <zha-device-endpoint-data-table
                  id="removeMembers"
                  .hass=${this.hass}
                  .deviceEndpoints=${this.group.members}
                  .narrow=${this.narrow}
                  selectable
                  @selection-changed=${this._handleRemoveSelectionChanged}
                >
                </zha-device-endpoint-data-table>

                <div class="buttons">
                  <mwc-button
                    .disabled=${!this._selectedDevicesToRemove.length||this._processingRemove}
                    @click=${this._removeMembersFromGroup}
                    class="button"
                  >
                    <ha-circular-progress
                      ?active=${this._processingRemove}
                      alt=${this.hass.localize("ui.panel.config.zha.groups.removing_members")}
                    ></ha-circular-progress>
                    ${this.hass.localize("ui.panel.config.zha.groups.remove_members")}</mwc-button
                  >
                </div>
              `:i.dy``}

          <div class="header">
            ${this.hass.localize("ui.panel.config.zha.groups.add_members")}
          </div>

          <zha-device-endpoint-data-table
            id="addMembers"
            .hass=${this.hass}
            .deviceEndpoints=${this._filteredDeviceEndpoints}
            .narrow=${this.narrow}
            selectable
            @selection-changed=${this._handleAddSelectionChanged}
          >
          </zha-device-endpoint-data-table>

          <div class="buttons">
            <mwc-button
              .disabled=${!this._selectedDevicesToAdd.length||this._processingAdd}
              @click=${this._addMembersToGroup}
              class="button"
            >
              ${this._processingAdd?i.dy`<ha-circular-progress
                    active
                    size="small"
                    title="Saving"
                  ></ha-circular-progress>`:""}
              ${this.hass.localize("ui.panel.config.zha.groups.add_members")}</mwc-button
            >
          </div>
        </ha-config-section>
      </hass-subpage>
    `:i.dy`
        <hass-error-screen
          .hass=${this.hass}
          .error=${this.hass.localize("ui.panel.config.zha.groups.group_not_found")}
        ></hass-error-screen>
      `}},{kind:"method",key:"_fetchData",value:async function(){null!==this.groupId&&void 0!==this.groupId&&(this.group=await(0,s.yi)(this.hass,this.groupId)),this.deviceEndpoints=await(0,s.pT)(this.hass),this._filterDevices()}},{kind:"method",key:"_filterDevices",value:function(){this._filteredDeviceEndpoints=this.deviceEndpoints.filter((e=>!this.group.members.some((t=>t.device.ieee===e.device.ieee&&t.endpoint_id===e.endpoint_id))))}},{kind:"method",key:"_handleAddSelectionChanged",value:function(e){this._selectedDevicesToAdd=e.detail.value}},{kind:"method",key:"_handleRemoveSelectionChanged",value:function(e){this._selectedDevicesToRemove=e.detail.value}},{kind:"method",key:"_addMembersToGroup",value:async function(){this._processingAdd=!0;const e=this._selectedDevicesToAdd.map((e=>{const t=e.split("_");return{ieee:t[0],endpoint_id:t[1]}}));this.group=await(0,s.dy)(this.hass,this.groupId,e),this._filterDevices(),this._selectedDevicesToAdd=[],this._zhaAddMembersDataTable.clearSelection(),this._processingAdd=!1}},{kind:"method",key:"_removeMembersFromGroup",value:async function(){this._processingRemove=!0;const e=this._selectedDevicesToRemove.map((e=>{const t=e.split("_");return{ieee:t[0],endpoint_id:t[1]}}));this.group=await(0,s.tz)(this.hass,this.groupId,e),this._filterDevices(),this._selectedDevicesToRemove=[],this._zhaRemoveMembersDataTable.clearSelection(),this._processingRemove=!1}},{kind:"method",key:"_deleteGroup",value:async function(){await(0,s.gg)(this.hass,[this.groupId]),(0,o.c)("/config/zha/groups",{replace:!0})}},{kind:"get",static:!0,key:"styles",value:function(){return[i.iv`
        hass-subpage {
          --app-header-text-color: var(--sidebar-icon-color);
        }
        .header {
          font-family: var(--paper-font-display1_-_font-family);
          -webkit-font-smoothing: var(
            --paper-font-display1_-_-webkit-font-smoothing
          );
          font-size: var(--paper-font-display1_-_font-size);
          font-weight: var(--paper-font-display1_-_font-weight);
          letter-spacing: var(--paper-font-display1_-_letter-spacing);
          line-height: var(--paper-font-display1_-_line-height);
          opacity: var(--dark-primary-opacity);
        }

        .button {
          float: right;
        }

        a {
          color: var(--primary-color);
          text-decoration: none;
        }
        .buttons {
          align-items: flex-end;
          padding: 8px;
        }
        .buttons .warning {
          --mdc-theme-primary: var(--error-color);
        }
      `]}}]}}),i.oi)},93217:function(e,t,r){r.d(t,{Ud:function(){return p}});const i=Symbol("Comlink.proxy"),n=Symbol("Comlink.endpoint"),o=Symbol("Comlink.releaseProxy"),s=Symbol("Comlink.finalizer"),a=Symbol("Comlink.thrown"),c=e=>"object"==typeof e&&null!==e||"function"==typeof e,l=new Map([["proxy",{canHandle:e=>c(e)&&e[i],serialize(e){const{port1:t,port2:r}=new MessageChannel;return d(e,t),[r,[r]]},deserialize(e){return e.start(),p(e)}}],["throw",{canHandle:e=>c(e)&&a in e,serialize({value:e}){let t;return t=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[t,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function d(e,t=globalThis,r=["*"]){t.addEventListener("message",(function n(o){if(!o||!o.data)return;if(!function(e,t){for(const r of e){if(t===r||"*"===r)return!0;if(r instanceof RegExp&&r.test(t))return!0}return!1}(r,o.origin))return void console.warn(`Invalid origin '${o.origin}' for comlink proxy`);const{id:c,type:l,path:p}=Object.assign({path:[]},o.data),h=(o.data.argumentList||[]).map(k);let f;try{const t=p.slice(0,-1).reduce(((e,t)=>e[t]),e),r=p.reduce(((e,t)=>e[t]),e);switch(l){case"GET":f=r;break;case"SET":t[p.slice(-1)[0]]=k(o.data.value),f=!0;break;case"APPLY":f=r.apply(t,h);break;case"CONSTRUCT":f=function(e){return Object.assign(e,{[i]:!0})}(new r(...h));break;case"ENDPOINT":{const{port1:t,port2:r}=new MessageChannel;d(e,r),f=function(e,t){return b.set(e,t),e}(t,[t])}break;case"RELEASE":f=void 0;break;default:return}}catch(m){f={value:m,[a]:0}}Promise.resolve(f).catch((e=>({value:e,[a]:0}))).then((r=>{const[i,o]=_(r);t.postMessage(Object.assign(Object.assign({},i),{id:c}),o),"RELEASE"===l&&(t.removeEventListener("message",n),u(t),s in e&&"function"==typeof e[s]&&e[s]())})).catch((e=>{const[r,i]=_({value:new TypeError("Unserializable return value"),[a]:0});t.postMessage(Object.assign(Object.assign({},r),{id:c}),i)}))})),t.start&&t.start()}function u(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function p(e,t){return g(e,[],t)}function h(e){if(e)throw new Error("Proxy has been released and is not useable")}function f(e){return w(e,{type:"RELEASE"}).then((()=>{u(e)}))}const m=new WeakMap,v="FinalizationRegistry"in globalThis&&new FinalizationRegistry((e=>{const t=(m.get(e)||0)-1;m.set(e,t),0===t&&f(e)}));function g(e,t=[],r=function(){}){let i=!1;const s=new Proxy(r,{get(r,n){if(h(i),n===o)return()=>{!function(e){v&&v.unregister(e)}(s),f(e),i=!0};if("then"===n){if(0===t.length)return{then:()=>s};const r=w(e,{type:"GET",path:t.map((e=>e.toString()))}).then(k);return r.then.bind(r)}return g(e,[...t,n])},set(r,n,o){h(i);const[s,a]=_(o);return w(e,{type:"SET",path:[...t,n].map((e=>e.toString())),value:s},a).then(k)},apply(r,o,s){h(i);const a=t[t.length-1];if(a===n)return w(e,{type:"ENDPOINT"}).then(k);if("bind"===a)return g(e,t.slice(0,-1));const[c,l]=y(s);return w(e,{type:"APPLY",path:t.map((e=>e.toString())),argumentList:c},l).then(k)},construct(r,n){h(i);const[o,s]=y(n);return w(e,{type:"CONSTRUCT",path:t.map((e=>e.toString())),argumentList:o},s).then(k)}});return function(e,t){const r=(m.get(t)||0)+1;m.set(t,r),v&&v.register(e,t,e)}(s,e),s}function y(e){const t=e.map(_);return[t.map((e=>e[0])),(r=t.map((e=>e[1])),Array.prototype.concat.apply([],r))];var r}const b=new WeakMap;function _(e){for(const[t,r]of l)if(r.canHandle(e)){const[i,n]=r.serialize(e);return[{type:"HANDLER",name:t,value:i},n]}return[{type:"RAW",value:e},b.get(e)||[]]}function k(e){switch(e.type){case"HANDLER":return l.get(e.name).deserialize(e.value);case"RAW":return e.value}}function w(e,t,r){return new Promise((i=>{const n=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");e.addEventListener("message",(function t(r){r.data&&r.data.id&&r.data.id===n&&(e.removeEventListener("message",t),i(r.data))})),e.start&&e.start(),e.postMessage(Object.assign({id:n},t),r)}))}},19596:function(e,t,r){r.d(t,{sR:function(){return u}});var i=r(81563),n=r(38941);const o=(e,t)=>{var r,i;const n=e._$AN;if(void 0===n)return!1;for(const s of n)null===(i=(r=s)._$AO)||void 0===i||i.call(r,t,!1),o(s,t);return!0},s=e=>{let t,r;do{if(void 0===(t=e._$AM))break;r=t._$AN,r.delete(e),e=t}while(0===(null==r?void 0:r.size))},a=e=>{for(let t;t=e._$AM;e=t){let r=t._$AN;if(void 0===r)t._$AN=r=new Set;else if(r.has(e))break;r.add(e),d(t)}};function c(e){void 0!==this._$AN?(s(this),this._$AM=e,a(this)):this._$AM=e}function l(e,t=!1,r=0){const i=this._$AH,n=this._$AN;if(void 0!==n&&0!==n.size)if(t)if(Array.isArray(i))for(let a=r;a<i.length;a++)o(i[a],!1),s(i[a]);else null!=i&&(o(i,!1),s(i));else o(this,e)}const d=e=>{var t,r,i,o;e.type==n.pX.CHILD&&(null!==(t=(i=e)._$AP)&&void 0!==t||(i._$AP=l),null!==(r=(o=e)._$AQ)&&void 0!==r||(o._$AQ=c))};class u extends n.Xe{constructor(){super(...arguments),this._$AN=void 0}_$AT(e,t,r){super._$AT(e,t,r),a(this),this.isConnected=e._$AU}_$AO(e,t=!0){var r,i;e!==this.isConnected&&(this.isConnected=e,e?null===(r=this.reconnected)||void 0===r||r.call(this):null===(i=this.disconnected)||void 0===i||i.call(this)),t&&(o(this,e),s(this))}setValue(e){if((0,i.OR)(this._$Ct))this._$Ct._$AI(e,this);else{const t=[...this._$Ct._$AH];t[this._$Ci]=e,this._$Ct._$AI(t,this,0)}}disconnected(){}reconnected(){}}},81563:function(e,t,r){r.d(t,{E_:function(){return v},OR:function(){return c},_Y:function(){return d},dZ:function(){return a},fk:function(){return u},hN:function(){return s},hl:function(){return h},i9:function(){return f},pt:function(){return o},ws:function(){return m}});var i=r(15304);const{I:n}=i._$LH,o=e=>null===e||"object"!=typeof e&&"function"!=typeof e,s=(e,t)=>void 0===t?void 0!==(null==e?void 0:e._$litType$):(null==e?void 0:e._$litType$)===t,a=e=>{var t;return null!=(null===(t=null==e?void 0:e._$litType$)||void 0===t?void 0:t.h)},c=e=>void 0===e.strings,l=()=>document.createComment(""),d=(e,t,r)=>{var i;const o=e._$AA.parentNode,s=void 0===t?e._$AB:t._$AA;if(void 0===r){const t=o.insertBefore(l(),s),i=o.insertBefore(l(),s);r=new n(t,i,e,e.options)}else{const t=r._$AB.nextSibling,n=r._$AM,a=n!==e;if(a){let t;null===(i=r._$AQ)||void 0===i||i.call(r,e),r._$AM=e,void 0!==r._$AP&&(t=e._$AU)!==n._$AU&&r._$AP(t)}if(t!==s||a){let e=r._$AA;for(;e!==t;){const t=e.nextSibling;o.insertBefore(e,s),e=t}}}return r},u=(e,t,r=e)=>(e._$AI(t,r),e),p={},h=(e,t=p)=>e._$AH=t,f=e=>e._$AH,m=e=>{var t;null===(t=e._$AP)||void 0===t||t.call(e,!1,!0);let r=e._$AA;const i=e._$AB.nextSibling;for(;r!==i;){const e=r.nextSibling;r.remove(),r=e}},v=e=>{e._$AR()}},57835:function(e,t,r){r.d(t,{XM:function(){return i.XM},Xe:function(){return i.Xe},pX:function(){return i.pX}});var i=r(38941)}}]);
//# sourceMappingURL=9fae1a89.js.map