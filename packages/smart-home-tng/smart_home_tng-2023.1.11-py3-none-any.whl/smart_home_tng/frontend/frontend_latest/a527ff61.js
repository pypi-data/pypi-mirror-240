"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[99528],{43793:(e,t,i)=>{i.d(t,{x:()=>r});const r=(e,t)=>e.substring(0,t.length)===t},99282:(e,t,i)=>{var r=i(52039);class n extends r.C{connectedCallback(){super.connectedCallback(),setTimeout((()=>{this.path="ltr"===window.getComputedStyle(this).direction?"M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z":"M15.41,16.58L10.83,12L15.41,7.41L14,6L8,12L14,18L15.41,16.58Z"}),100)}}customElements.define("ha-icon-next",n)},55422:(e,t,i)=>{i.a(e,(async(e,r)=>{try{i.d(t,{MY:()=>k,Yc:()=>y,hb:()=>g,jV:()=>u,o1:()=>v,ri:()=>b,sS:()=>m,tf:()=>_});var n=i(49706),s=i(58831),o=i(29171),a=i(22311),c=i(56007),l=e([o]);o=(l.then?(await l)():l)[0];const d="ui.components.logbook.messages",u=["counter","proximity","sensor","zone"],h={"numeric state of":"triggered_by_numeric_state_of","state of":"triggered_by_state_of",event:"triggered_by_event",time:"triggered_by_time","time pattern":"triggered_by_time_pattern","Home Assistant stopping":"triggered_by_homeassistant_stopping","Home Assistant starting":"triggered_by_homeassistant_starting"},p={},m=async(e,t,i)=>(await e.loadBackendTranslation("device_class"),f(e,t,void 0,void 0,i)),f=(e,t,i,r,n,s)=>{if((r||s)&&(!r||0===r.length)&&(!s||0===s.length))return Promise.resolve([]);const o={type:"logbook/get_events",start_time:t};return i&&(o.end_time=i),null!=r&&r.length&&(o.entity_ids=r),null!=s&&s.length&&(o.device_ids=s),n&&(o.context_id=n),e.callWS(o)},y=(e,t,i,r,n,s)=>{if((n||s)&&(!n||0===n.length)&&(!s||0===s.length))return Promise.reject("No entities or devices");const o={type:"logbook/event_stream",start_time:i,end_time:r};return null!=n&&n.length&&(o.entity_ids=n),null!=s&&s.length&&(o.device_ids=s),e.connection.subscribeMessage((e=>t(e)),o)},_=(e,t)=>{p[`${e}${t}`]={}},v=(e,t)=>({entity_id:e.entity_id,state:t,attributes:{device_class:null==e?void 0:e.attributes.device_class,source_type:null==e?void 0:e.attributes.source_type,has_date:null==e?void 0:e.attributes.has_date,has_time:null==e?void 0:e.attributes.has_time,entity_picture_local:n.iY.has((0,s.M)(e.entity_id))||null==e?void 0:e.attributes.entity_picture_local,entity_picture:n.iY.has((0,s.M)(e.entity_id))||null==e?void 0:e.attributes.entity_picture}}),g=(e,t)=>{for(const i in h)if(t.startsWith(i))return t.replace(i,`${e(`ui.components.logbook.${h[i]}`)}`);return t},b=(e,t,i,r,s)=>{switch(s){case"device_tracker":case"person":return"not_home"===i?t(`${d}.was_away`):"home"===i?t(`${d}.was_at_home`):t(`${d}.was_at_state`,"state",i);case"sun":return t("above_horizon"===i?`${d}.rose`:`${d}.set`);case"binary_sensor":{const e=i===n.uo,s=i===n.lC,o=r.attributes.device_class;switch(o){case"battery":if(e)return t(`${d}.was_low`);if(s)return t(`${d}.was_normal`);break;case"connectivity":if(e)return t(`${d}.was_connected`);if(s)return t(`${d}.was_disconnected`);break;case"door":case"garage_door":case"opening":case"window":if(e)return t(`${d}.was_opened`);if(s)return t(`${d}.was_closed`);break;case"lock":if(e)return t(`${d}.was_unlocked`);if(s)return t(`${d}.was_locked`);break;case"plug":if(e)return t(`${d}.was_plugged_in`);if(s)return t(`${d}.was_unplugged`);break;case"presence":if(e)return t(`${d}.was_at_home`);if(s)return t(`${d}.was_away`);break;case"safety":if(e)return t(`${d}.was_unsafe`);if(s)return t(`${d}.was_safe`);break;case"cold":case"gas":case"heat":case"moisture":case"motion":case"occupancy":case"power":case"problem":case"smoke":case"sound":case"vibration":if(e)return t(`${d}.detected_device_class`,{device_class:t(`component.binary_sensor.device_class.${o}`)});if(s)return t(`${d}.cleared_device_class`,{device_class:t(`component.binary_sensor.device_class.${o}`)});break;case"tamper":if(e)return t(`${d}.detected_tampering`);if(s)return t(`${d}.cleared_tampering`)}break}case"cover":switch(i){case"open":return t(`${d}.was_opened`);case"opening":return t(`${d}.is_opening`);case"closing":return t(`${d}.is_closing`);case"closed":return t(`${d}.was_closed`)}break;case"lock":if("unlocked"===i)return t(`${d}.was_unlocked`);if("locked"===i)return t(`${d}.was_locked`)}return i===n.uo?t(`${d}.turned_on`):i===n.lC?t(`${d}.turned_off`):c.V_.includes(i)?t(`${d}.became_unavailable`):e.localize(`${d}.changed_to_state`,"state",r?(0,o.D)(t,r,e.locale,i):i)},k=e=>"sensor"!==(0,a.N)(e)||void 0===e.attributes.unit_of_measurement&&void 0===e.attributes.state_class;r()}catch(e){r(e)}}))},97389:(e,t,i)=>{if(i.d(t,{U_:()=>o,Zm:()=>c,lj:()=>s,mA:()=>n,nV:()=>a}),32143==i.j)var r=i(43793);const n=(e,t,i,r)=>e.callWS({type:"trace/get",domain:t,item_id:i,run_id:r}),s=(e,t,i)=>e.callWS({type:"trace/list",domain:t,item_id:i}),o=(e,t,i)=>e.callWS({type:"trace/contexts",domain:t,item_id:i}),a=(e,t)=>{const i=t.split("/").reverse();let r=e;for(;i.length;){const e=i.pop(),t=Number(e);if(isNaN(t)){const t=r[e];if(!t&&"sequence"===e)continue;r=t}else if(Array.isArray(r))r=r[t];else if(0!==t)throw new Error("If config is not an array, can only return index 0")}return r},c=e=>"trigger"===e||(0,r.x)(e,"trigger/")},44198:(e,t,i)=>{i.a(e,(async(e,t)=>{try{i(86175);var r=i(37500),n=i(36924),s=i(8636),o=i(12198),a=i(49684),c=i(25516),l=i(47181),d=i(58831),u=i(7323),h=(i(3143),i(31206),i(42952)),p=i(55422),m=i(11654),f=i(11254),y=(i(99282),i(83849)),_=e([o,a,h,p]);function v(e,t,i,r){var n=g();if(r)for(var s=0;s<r.length;s++)n=r[s](n);var o=t((function(e){n.initializeInstanceElements(e,a.elements)}),i),a=n.decorateClass(w(o.d.map(b)),e);return n.initializeClassElements(o.F,a.elements),n.runClassFinishers(o.F,a.finishers)}function g(){g=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var s="static"===n?e:i;this.defineClassElement(s,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!x(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var s=this.decorateConstructor(i,t);return r.push.apply(r,s.finishers),s.finishers=r,s},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,s=n.length-1;s>=0;s--){var o=t[e.placement];o.splice(o.indexOf(e.key),1);var a=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,n[s])(a)||a);e=c.element,this.addElementPlacement(e,t),c.finisher&&r.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);i.push.apply(i,l)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),s=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==s.finisher&&i.push(s.finisher),void 0!==s.elements){e=s.elements;for(var o=0;o<e.length-1;o++)for(var a=o+1;a<e.length;a++)if(e[o].key===e[a].key&&e[o].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[o].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,T(t)||A(t)||S(t)||P()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=C(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var s={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),s.initializer=e.initializer),s},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:E(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=E(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function b(e){var t,i=C(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function k(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function w(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===s.key&&e.placement===s.placement},r=0;r<e.length;r++){var n,s=e[r];if("method"===s.kind&&(n=t.find(i)))if($(s.descriptor)||$(n.descriptor)){if(x(s)||x(n))throw new ReferenceError("Duplicated methods ("+s.key+") can't be decorated.");n.descriptor=s.descriptor}else{if(x(s)){if(x(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+s.key+").");n.decorators=s.decorators}k(s,n)}else t.push(s)}return t}function x(e){return e.decorators&&e.decorators.length}function $(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function E(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function C(e){var t=z(e,"string");return"symbol"==typeof t?t:String(t)}function z(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}function P(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function S(e,t){if(e){if("string"==typeof e)return D(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?D(e,t):void 0}}function D(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function A(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}function T(e){if(Array.isArray(e))return e}[o,a,h,p]=_.then?(await _)():_;const I=["script","automation"],M=e=>e.context_event_type||e.context_state||e.context_message,L=(e,t)=>t?e.replace(t," "):e;v([(0,n.Mo)("ha-logbook-renderer")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"userIdToName",value:()=>({})},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"traceContexts",value:()=>({})},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"entries",value:()=>[]},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"narrow"})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"virtualize",reflect:!0})],key:"virtualize",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"no-icon"})],key:"noIcon",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"no-name"})],key:"noName",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"relative-time"})],key:"relativeTime",value:()=>!1},{kind:"field",decorators:[(0,c.i)(".container")],key:"_savedScrollPos",value:void 0},{kind:"method",key:"shouldUpdate",value:function(e){const t=e.get("hass"),i=void 0===t||t.locale!==this.hass.locale;return e.has("entries")||e.has("traceContexts")||i}},{kind:"method",key:"render",value:function(){var e;return null!==(e=this.entries)&&void 0!==e&&e.length?r.dy`
      <div
        class="container ha-scrollbar ${(0,s.$)({narrow:this.narrow,"no-name":this.noName,"no-icon":this.noIcon})}"
        @scroll=${this._saveScrollPos}
      >
        ${this.virtualize?r.dy`<lit-virtualizer
              @visibilityChanged=${this._visibilityChanged}
              scroller
              class="ha-scrollbar"
              .items=${this.entries}
              .renderItem=${this._renderLogbookItem}
            >
            </lit-virtualizer>`:this.entries.map(((e,t)=>this._renderLogbookItem(e,t)))}
      </div>
    `:r.dy`
        <div class="container no-entries">
          ${this.hass.localize("ui.components.logbook.entries_not_found")}
        </div>
      `}},{kind:"field",key:"_renderLogbookItem",value(){return(e,t)=>{var i;if(!e||void 0===t)return r.dy``;const n=this.entries[t-1],c=[],l=e.entity_id?this.hass.states[e.entity_id]:void 0,h=l?(0,p.o1)(l,e.state):void 0,m=e.entity_id?(0,d.M)(e.entity_id):e.domain,y=h||e.icon||e.state||!m||!(0,u.p)(this.hass,m)?void 0:(0,f.X1)({domain:m,type:"icon",useFallback:!0,darkOptimized:null===(i=this.hass.themes)||void 0===i?void 0:i.darkMode}),_=I.includes(e.domain)&&e.context_id in this.traceContexts?this.traceContexts[e.context_id]:void 0,v=void 0!==_;return r.dy`
      <div
        class="entry-container ${(0,s.$)({clickable:v})}"
        .traceLink=${_?`/config/${_.domain}/trace/${"script"===_.domain?`script.${_.item_id}`:_.item_id}?run_id=${_.run_id}`:void 0}
        @click=${this._handleClick}
      >
        ${0===t||null!=e&&e.when&&null!=n&&n.when&&new Date(1e3*e.when).toDateString()!==new Date(1e3*n.when).toDateString()?r.dy`
              <h4 class="date">
                ${(0,o.p6)(new Date(1e3*e.when),this.hass.locale)}
              </h4>
            `:r.dy``}

        <div class="entry ${(0,s.$)({"no-entity":!e.entity_id})}">
          <div class="icon-message">
            ${this.noIcon?"":r.dy`
                  <state-badge
                    .hass=${this.hass}
                    .overrideIcon=${e.icon}
                    .overrideImage=${y}
                    .stateObj=${e.icon?void 0:h}
                    .stateColor=${!1}
                  ></state-badge>
                `}
            <div class="message-relative_time">
              <div class="message">
                ${this.noName?"":this._renderEntity(e.entity_id,e.name,v)}
                ${this._renderMessage(e,c,m,h,v)}
                ${this._renderContextMessage(e,c,v)}
              </div>
              <div class="secondary">
                <span
                  >${(0,a.Vu)(new Date(1e3*e.when),this.hass.locale)}</span
                >
                -
                <ha-relative-time
                  .hass=${this.hass}
                  .datetime=${1e3*e.when}
                  capitalize
                ></ha-relative-time>
                ${e.context_user_id?r.dy`${this._renderUser(e)}`:""}
                ${v?`- ${this.hass.localize("ui.components.logbook.show_trace")}`:""}
              </div>
            </div>
          </div>
          ${v?r.dy`<ha-icon-next></ha-icon-next>`:""}
        </div>
      </div>
    `}}},{kind:"method",decorators:[(0,n.hO)({passive:!0})],key:"_saveScrollPos",value:function(e){this._savedScrollPos=e.target.scrollTop}},{kind:"method",decorators:[(0,n.hO)({passive:!0})],key:"_visibilityChanged",value:function(e){(0,l.B)(this,"hass-logbook-live",{enable:0===e.first})}},{kind:"method",key:"_renderMessage",value:function(e,t,i,r,n){if(e.entity_id&&e.state)return r?(0,p.ri)(this.hass,this.hass.localize,e.state,r,i):e.state;const s=M(e);let o=e.message;if(I.includes(i)&&e.source){if(s)return"";o=(0,p.hb)(this.hass.localize,e.source)}return o?this._formatMessageWithPossibleEntity(s?L(o,e.context_entity_id):o,t,void 0,n):""}},{kind:"method",key:"_renderUser",value:function(e){const t=e.context_user_id&&this.userIdToName[e.context_user_id];return t?`- ${t}`:""}},{kind:"method",key:"_renderUnseenContextSourceEntity",value:function(e,t,i){return!e.context_entity_id||t.includes(e.context_entity_id)?"":r.dy` (${this._renderEntity(e.context_entity_id,e.context_entity_id_name,i)})`}},{kind:"method",key:"_renderContextMessage",value:function(e,t,i){if(e.context_state){const t=e.context_entity_id&&e.context_entity_id in this.hass.states?(0,p.o1)(this.hass.states[e.context_entity_id],e.context_state):void 0;return r.dy`${this.hass.localize("ui.components.logbook.triggered_by_state_of")}
      ${this._renderEntity(e.context_entity_id,e.context_entity_id_name,i)}
      ${t?(0,p.ri)(this.hass,this.hass.localize,e.context_state,t,(0,d.M)(e.context_entity_id)):e.context_state}`}if("call_service"===e.context_event_type)return r.dy`${this.hass.localize("ui.components.logbook.triggered_by_service")}
      ${e.context_domain}.${e.context_service}`;if(!e.context_message||t.includes(e.context_entity_id))return"";if("automation_triggered"===e.context_event_type||"script_started"===e.context_event_type){const n=e.context_source?e.context_source:e.context_message.replace("triggered by ",""),s=(0,p.hb)(this.hass.localize,n);return r.dy`${this.hass.localize("automation_triggered"===e.context_event_type?"ui.components.logbook.triggered_by_automation":"ui.components.logbook.triggered_by_script")}
      ${this._renderEntity(e.context_entity_id,e.context_entity_id_name,i)}
      ${e.context_message?this._formatMessageWithPossibleEntity(s,t,void 0,i):""}`}return r.dy` ${this.hass.localize("ui.components.logbook.triggered_by")}
    ${e.context_name}
    ${this._formatMessageWithPossibleEntity(e.context_message,t,e.context_entity_id,i)}
    ${this._renderUnseenContextSourceEntity(e,t,i)}`}},{kind:"method",key:"_renderEntity",value:function(e,t,i){const n=e&&e in this.hass.states,s=t||n&&this.hass.states[e].attributes.friendly_name||e;return n?i?s:r.dy`<button
          class="link"
          @click=${this._entityClicked}
          .entityId=${e}
        >
          ${s}
        </button>`:s}},{kind:"method",key:"_formatMessageWithPossibleEntity",value:function(e,t,i,n){if(-1!==e.indexOf(".")){const i=e.split(" ");for(let e=0,s=i.length;e<s;e++)if(i[e]in this.hass.states){const s=i[e];if(t.includes(s))return"";t.push(s);const o=i.splice(e);return o.shift(),r.dy`${i.join(" ")}
          ${this._renderEntity(s,this.hass.states[s].attributes.friendly_name,n)}
          ${o.join(" ")}`}}if(i&&i in this.hass.states){const s=this.hass.states[i].attributes.friendly_name;if(s&&e.endsWith(s))return t.includes(i)?"":(t.push(i),e=e.substring(0,e.length-s.length),r.dy`${e}
        ${this._renderEntity(i,s,n)}`)}return e}},{kind:"method",key:"_entityClicked",value:function(e){const t=e.currentTarget.entityId;t&&(e.preventDefault(),e.stopPropagation(),(0,l.B)(this,"hass-more-info",{entityId:t}))}},{kind:"method",key:"_handleClick",value:function(e){e.currentTarget.traceLink&&((0,y.c)(e.currentTarget.traceLink),(0,l.B)(this,"closed"))}},{kind:"get",static:!0,key:"styles",value:function(){return[m.Qx,m.$c,m.k1,r.iv`
        :host([virtualize]) {
          display: block;
          height: 100%;
        }

        .entry-container {
          width: 100%;
        }

        .entry {
          display: flex;
          width: 100%;
          line-height: 2em;
          padding: 8px 16px;
          box-sizing: border-box;
          border-top: 1px solid var(--divider-color);
          justify-content: space-between;
          align-items: center;
        }

        ha-icon-next {
          color: var(--secondary-text-color);
        }

        .clickable {
          cursor: pointer;
        }

        :not(.clickable) .entry.no-entity,
        :not(.clickable) .no-name .entry {
          cursor: default;
        }

        .entry:hover {
          background-color: rgba(var(--rgb-primary-text-color), 0.04);
        }

        .narrow:not(.no-icon) .time {
          margin-left: 32px;
          margin-inline-start: 32px;
          margin-inline-end: initial;
          direction: var(--direction);
        }

        .message-relative_time {
          display: flex;
          flex-direction: column;
        }

        .secondary {
          font-size: 12px;
          line-height: 1.7;
        }

        .secondary a {
          color: var(--secondary-text-color);
        }

        .date {
          margin: 8px 0;
          padding: 0 16px;
        }

        .icon-message {
          display: flex;
          align-items: center;
        }

        .no-entries {
          text-align: center;
          color: var(--secondary-text-color);
        }

        state-badge {
          margin-right: 16px;
          margin-inline-start: initial;
          flex-shrink: 0;
          color: var(--state-icon-color);
          margin-inline-end: 16px;
          direction: var(--direction);
        }

        .message {
          color: var(--primary-text-color);
        }

        .no-name .message:first-letter {
          text-transform: capitalize;
        }

        a {
          color: var(--primary-color);
          text-decoration: none;
        }

        button.link {
          color: var(--paper-item-icon-color);
          text-decoration: none;
        }

        .container {
          max-height: var(--logbook-max-height);
        }

        .container,
        lit-virtualizer {
          height: 100%;
        }

        lit-virtualizer {
          contain: size layout !important;
        }

        .narrow .entry {
          line-height: 1.5;
        }

        .narrow .icon-message state-badge {
          margin-left: 0;
          margin-inline-start: 0;
          margin-inline-end: 8px;
          margin-right: 8px;
          direction: var(--direction);
        }
      `]}}]}}),r.oi);t()}catch(j){t(j)}}))}}]);
//# sourceMappingURL=a527ff61.js.map