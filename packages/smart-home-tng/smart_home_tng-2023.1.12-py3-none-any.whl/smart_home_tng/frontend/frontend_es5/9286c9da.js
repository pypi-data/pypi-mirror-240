"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[15101],{5435:function(t,e,i){i.d(e,{G:function(){return n}});var r=i(14516);i(92874);const o=(0,r.Z)((t=>new Intl.RelativeTimeFormat(t.language,{numeric:"auto"}))),n=(t,e,i,r=!0)=>{const n=function(t,e,i){void 0===e&&(e=new Date);void 0===i&&(i=h);var r=(+t-+e)/a;if(Math.abs(r)<i.second)return{value:Math.round(r),unit:"second"};var o=r/s;if(Math.abs(o)<i.minute)return{value:Math.round(o),unit:"minute"};var n=r/c;if(Math.abs(n)<i.hour)return{value:Math.round(n),unit:"hour"};var u=r/l;if(Math.abs(u)<i.day)return{value:Math.round(u),unit:"day"};var p=new Date(t),f=new Date(e),v=p.getFullYear()-f.getFullYear();if(Math.round(Math.abs(v))>0)return{value:Math.round(v),unit:"year"};var m=12*v+p.getMonth()-f.getMonth();if(Math.round(Math.abs(m))>0)return{value:Math.round(m),unit:"month"};var y=r/d;return{value:Math.round(y),unit:"week"}}(t,i);return r?o(e).format(n.value,n.unit):Intl.NumberFormat(e.language,{style:"unit",unit:n.unit,unitDisplay:"long"}).format(Math.abs(n.value))},a=1e3,s=60,c=60*s,l=24*c,d=7*l;const h={second:45,minute:45,hour:22,day:5}},67876:function(t,e,i){i.r(e),i.d(e,{HaScriptTrace:function(){return I}});var r=i(37500),o=i(36924),n=i(8636),a=i(86230),s=i(7323),c=i(44583),l=(i(10983),i(71955),i(13126),i(89497),i(78940),i(79459),i(54933),i(19476)),d=i(55422),h=i(97389),u=i(26765),p=i(11654),f=(i(60010),i(81545),i(47181));function v(){v=function(){return t};var t={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(t,e){["method","field"].forEach((function(i){e.forEach((function(e){e.kind===i&&"own"===e.placement&&this.defineClassElement(t,e)}),this)}),this)},initializeClassElements:function(t,e){var i=t.prototype;["method","field"].forEach((function(r){e.forEach((function(e){var o=e.placement;if(e.kind===r&&("static"===o||"prototype"===o)){var n="static"===o?t:i;this.defineClassElement(n,e)}}),this)}),this)},defineClassElement:function(t,e){var i=e.descriptor;if("field"===e.kind){var r=e.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(t)}}Object.defineProperty(t,e.key,i)},decorateClass:function(t,e){var i=[],r=[],o={static:[],prototype:[],own:[]};if(t.forEach((function(t){this.addElementPlacement(t,o)}),this),t.forEach((function(t){if(!k(t))return i.push(t);var e=this.decorateElement(t,o);i.push(e.element),i.push.apply(i,e.extras),r.push.apply(r,e.finishers)}),this),!e)return{elements:i,finishers:r};var n=this.decorateConstructor(i,e);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(t,e,i){var r=e[t.placement];if(!i&&-1!==r.indexOf(t.key))throw new TypeError("Duplicated element ("+t.key+")");r.push(t.key)},decorateElement:function(t,e){for(var i=[],r=[],o=t.decorators,n=o.length-1;n>=0;n--){var a=e[t.placement];a.splice(a.indexOf(t.key),1);var s=this.fromElementDescriptor(t),c=this.toElementFinisherExtras((0,o[n])(s)||s);t=c.element,this.addElementPlacement(t,e),c.finisher&&r.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],e);i.push.apply(i,l)}}return{element:t,finishers:r,extras:i}},decorateConstructor:function(t,e){for(var i=[],r=e.length-1;r>=0;r--){var o=this.fromClassDescriptor(t),n=this.toClassDescriptor((0,e[r])(o)||o);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){t=n.elements;for(var a=0;a<t.length-1;a++)for(var s=a+1;s<t.length;s++)if(t[a].key===t[s].key&&t[a].placement===t[s].placement)throw new TypeError("Duplicated element ("+t[a].key+")")}}return{elements:t,finishers:i}},fromElementDescriptor:function(t){var e={kind:t.kind,key:t.key,placement:t.placement,descriptor:t.descriptor};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===t.kind&&(e.initializer=t.initializer),e},toElementDescriptors:function(t){var e;if(void 0!==t)return(e=t,function(t){if(Array.isArray(t))return t}(e)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(e)||function(t,e){if(t){if("string"==typeof t)return w(t,e);var i=Object.prototype.toString.call(t).slice(8,-1);return"Object"===i&&t.constructor&&(i=t.constructor.name),"Map"===i||"Set"===i?Array.from(t):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?w(t,e):void 0}}(e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(t){var e=this.toElementDescriptor(t);return this.disallowProperty(t,"finisher","An element descriptor"),this.disallowProperty(t,"extras","An element descriptor"),e}),this)},toElementDescriptor:function(t){var e=String(t.kind);if("method"!==e&&"field"!==e)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+e+'"');var i=_(t.key),r=String(t.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var o=t.descriptor;this.disallowProperty(t,"elements","An element descriptor");var n={kind:e,key:i,placement:r,descriptor:Object.assign({},o)};return"field"!==e?this.disallowProperty(t,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=t.initializer),n},toElementFinisherExtras:function(t){return{element:this.toElementDescriptor(t),finisher:b(t,"finisher"),extras:this.toElementDescriptors(t.extras)}},fromClassDescriptor:function(t){var e={kind:"class",elements:t.map(this.fromElementDescriptor,this)};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),e},toClassDescriptor:function(t){var e=String(t.kind);if("class"!==e)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+e+'"');this.disallowProperty(t,"key","A class descriptor"),this.disallowProperty(t,"placement","A class descriptor"),this.disallowProperty(t,"descriptor","A class descriptor"),this.disallowProperty(t,"initializer","A class descriptor"),this.disallowProperty(t,"extras","A class descriptor");var i=b(t,"finisher");return{elements:this.toElementDescriptors(t.elements),finisher:i}},runClassFinishers:function(t,e){for(var i=0;i<e.length;i++){var r=(0,e[i])(t);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");t=r}}return t},disallowProperty:function(t,e,i){if(void 0!==t[e])throw new TypeError(i+" can't have a ."+e+" property.")}};return t}function m(t){var e,i=_(t.key);"method"===t.kind?e={value:t.value,writable:!0,configurable:!0,enumerable:!1}:"get"===t.kind?e={get:t.value,configurable:!0,enumerable:!1}:"set"===t.kind?e={set:t.value,configurable:!0,enumerable:!1}:"field"===t.kind&&(e={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===t.kind?"field":"method",key:i,placement:t.static?"static":"field"===t.kind?"own":"prototype",descriptor:e};return t.decorators&&(r.decorators=t.decorators),"field"===t.kind&&(r.initializer=t.value),r}function y(t,e){void 0!==t.descriptor.get?e.descriptor.get=t.descriptor.get:e.descriptor.set=t.descriptor.set}function k(t){return t.decorators&&t.decorators.length}function g(t){return void 0!==t&&!(void 0===t.value&&void 0===t.writable)}function b(t,e){var i=t[e];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+e+"' to be a function");return i}function _(t){var e=function(t,e){if("object"!=typeof t||null===t)return t;var i=t[Symbol.toPrimitive];if(void 0!==i){var r=i.call(t,e||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===e?String:Number)(t)}(t,"string");return"symbol"==typeof e?e:String(e)}function w(t,e){(null==e||e>t.length)&&(e=t.length);for(var i=0,r=new Array(e);i<e;i++)r[i]=t[i];return r}function E(){return E="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(t,e,i){var r=function(t,e){for(;!Object.prototype.hasOwnProperty.call(t,e)&&null!==(t=$(t)););return t}(t,e);if(r){var o=Object.getOwnPropertyDescriptor(r,e);return o.get?o.get.call(arguments.length<3?t:i):o.value}},E.apply(this,arguments)}function $(t){return $=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},$(t)}let I=function(t,e,i,r){var o=v();if(r)for(var n=0;n<r.length;n++)o=r[n](o);var a=e((function(t){o.initializeInstanceElements(t,s.elements)}),i),s=o.decorateClass(function(t){for(var e=[],i=function(t){return"method"===t.kind&&t.key===n.key&&t.placement===n.placement},r=0;r<t.length;r++){var o,n=t[r];if("method"===n.kind&&(o=e.find(i)))if(g(n.descriptor)||g(o.descriptor)){if(k(n)||k(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(k(n)){if(k(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}y(n,o)}else e.push(n)}return e}(a.d.map(m)),t);return o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,o.Mo)("ha-script-trace")],(function(t,e){class i extends e{constructor(...e){super(...e),t(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"scriptEntityId",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"scripts",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"route",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_traces",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_runId",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_selected",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_trace",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_logbookEntries",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_view",value(){return"details"}},{kind:"field",decorators:[(0,o.IO)("hat-script-graph")],key:"_graph",value:void 0},{kind:"method",key:"render",value:function(){var t;const e=this.scriptEntityId?this.hass.states[this.scriptEntityId]:void 0,i=this._graph,o=null==i?void 0:i.trackedNodes,s=null==i?void 0:i.renderedNodes,l=(null==e?void 0:e.attributes.friendly_name)||this.scriptEntityId;return r.dy`
      ${""}
      <hass-subpage .hass=${this.hass} .narrow=${this.narrow} .header=${l}>
        ${!this.narrow&&this.scriptEntityId?r.dy`
              <a
                class="trace-link"
                href="/config/script/edit/${this.scriptEntityId}"
                slot="toolbar-icon"
              >
                <mwc-button>
                  ${this.hass.localize("ui.panel.config.script.trace.edit_script")}
                </mwc-button>
              </a>
            `:""}

        <ha-button-menu corner="BOTTOM_START" slot="toolbar-icon">
          <ha-icon-button
            slot="trigger"
            .label=${this.hass.localize("ui.common.menu")}
            .path=${"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z"}
          ></ha-icon-button>

          <mwc-list-item
            graphic="icon"
            .disabled=${!this.scriptEntityId}
            @click=${this._showInfo}
          >
            ${this.hass.localize("ui.panel.config.script.editor.show_info")}
            <ha-svg-icon
              slot="graphic"
              .path=${"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z"}
            ></ha-svg-icon>
          </mwc-list-item>

          ${this.narrow&&this.scriptEntityId?r.dy`
                <a
                  class="trace-link"
                  href="/config/script/edit/${this.scriptEntityId}"
                >
                  <mwc-list-item graphic="icon">
                    ${this.hass.localize("ui.panel.config.script.trace.edit_script")}
                    <ha-svg-icon
                      slot="graphic"
                      .path=${"M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"}
                    ></ha-svg-icon>
                  </mwc-list-item>
                </a>
              `:""}

          <li divider role="separator"></li>

          <mwc-list-item graphic="icon" @click=${this._refreshTraces}>
            ${this.hass.localize("ui.panel.config.automation.trace.refresh")}
            <ha-svg-icon slot="graphic" .path=${"M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z"}></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            graphic="icon"
            .disabled=${!this._trace}
            @click=${this._downloadTrace}
          >
            ${this.hass.localize("ui.panel.config.automation.trace.download_trace")}
            <ha-svg-icon slot="graphic" .path=${"M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z"}></ha-svg-icon>
          </mwc-list-item>
        </ha-button-menu>

        <div class="toolbar">
          ${this._traces&&this._traces.length>0?r.dy`
                <ha-icon-button
                  .disabled=${this._traces[this._traces.length-1].run_id===this._runId}
                  label="Older trace"
                  @click=${this._pickOlderTrace}
                  .path=${"M1,12L5,16V13H17.17C17.58,14.17 18.69,15 20,15A3,3 0 0,0 23,12A3,3 0 0,0 20,9C18.69,9 17.58,9.83 17.17,11H5V8L1,12Z"}
                ></ha-icon-button>
                <select .value=${this._runId} @change=${this._pickTrace}>
                  ${(0,a.r)(this._traces,(t=>t.run_id),(t=>r.dy`<option value=${t.run_id}>
                        ${(0,c.E8)(new Date(t.timestamp.start),this.hass.locale)}
                      </option>`))}
                </select>
                <ha-icon-button
                  .disabled=${this._traces[0].run_id===this._runId}
                  label="Newer trace"
                  @click=${this._pickNewerTrace}
                  .path=${"M23,12L19,16V13H6.83C6.42,14.17 5.31,15 4,15A3,3 0 0,1 1,12A3,3 0 0,1 4,9C5.31,9 6.42,9.83 6.83,11H19V8L23,12Z"}
                ></ha-icon-button>
              `:""}
        </div>

        ${void 0===this._traces?r.dy`<div class="container">Loading…</div>`:0===this._traces.length?r.dy`<div class="container">No traces found</div>`:void 0===this._trace?"":r.dy`
              <div class="main">
                <div class="graph">
                  <hat-script-graph
                    .trace=${this._trace}
                    .selected=${null===(t=this._selected)||void 0===t?void 0:t.path}
                    @graph-node-selected=${this._pickNode}
                  ></hat-script-graph>
                </div>

                <div class="info">
                  <div class="tabs top">
                    ${[["details","Step Details"],["timeline","Trace Timeline"],["logbook","Related logbook entries"],["config","Script Config"]].map((([t,e])=>r.dy`
                        <button
                          tabindex="0"
                          .view=${t}
                          class=${(0,n.$)({active:this._view===t})}
                          @click=${this._showTab}
                        >
                          ${e}
                        </button>
                      `))}
                    ${this._trace.blueprint_inputs?r.dy`
                          <button
                            tabindex="0"
                            .view=${"blueprint"}
                            class=${(0,n.$)({active:"blueprint"===this._view})}
                            @click=${this._showTab}
                          >
                            Blueprint Config
                          </button>
                        `:""}
                  </div>
                  ${void 0===this._selected||void 0===this._logbookEntries||void 0===o?"":"details"===this._view?r.dy`
                        <ha-trace-path-details
                          .hass=${this.hass}
                          .narrow=${this.narrow}
                          .trace=${this._trace}
                          .selected=${this._selected}
                          .logbookEntries=${this._logbookEntries}
                          .trackedNodes=${o}
                          .renderedNodes=${s}
                        ></ha-trace-path-details>
                      `:"config"===this._view?r.dy`
                        <ha-trace-config
                          .hass=${this.hass}
                          .trace=${this._trace}
                        ></ha-trace-config>
                      `:"logbook"===this._view?r.dy`
                        <ha-trace-logbook
                          .hass=${this.hass}
                          .narrow=${this.narrow}
                          .trace=${this._trace}
                          .logbookEntries=${this._logbookEntries}
                        ></ha-trace-logbook>
                      `:"blueprint"===this._view?r.dy`
                        <ha-trace-blueprint-config
                          .hass=${this.hass}
                          .trace=${this._trace}
                        ></ha-trace-blueprint-config>
                      `:r.dy`
                        <ha-trace-timeline
                          .hass=${this.hass}
                          .trace=${this._trace}
                          .logbookEntries=${this._logbookEntries}
                          .selected=${this._selected}
                          @value-changed=${this._timelinePathPicked}
                        ></ha-trace-timeline>
                      `}
                </div>
              </div>
            `}
      </hass-subpage>
    `}},{kind:"method",key:"firstUpdated",value:function(t){if(E($(i.prototype),"firstUpdated",this).call(this,t),!this.scriptEntityId)return;const e=new URLSearchParams(location.search);this._loadTraces(e.get("run_id")||void 0)}},{kind:"method",key:"willUpdate",value:function(t){E($(i.prototype),"willUpdate",this).call(this,t),t.get("scriptEntityId")&&(this._traces=void 0,this._runId=void 0,this._trace=void 0,this._logbookEntries=void 0,this.scriptEntityId&&this._loadTraces()),t.has("_runId")&&this._runId&&(this._trace=void 0,this._logbookEntries=void 0,this._loadTrace())}},{kind:"method",key:"_pickOlderTrace",value:function(){const t=this._traces.findIndex((t=>t.run_id===this._runId));this._runId=this._traces[t+1].run_id,this._selected=void 0}},{kind:"method",key:"_pickNewerTrace",value:function(){const t=this._traces.findIndex((t=>t.run_id===this._runId));this._runId=this._traces[t-1].run_id,this._selected=void 0}},{kind:"method",key:"_pickTrace",value:function(t){this._runId=t.target.value,this._selected=void 0}},{kind:"method",key:"_pickNode",value:function(t){this._selected=t.detail}},{kind:"method",key:"_refreshTraces",value:function(){this._loadTraces()}},{kind:"method",key:"_loadTraces",value:async function(t){if(this._traces=await(0,h.lj)(this.hass,"script",this.scriptEntityId.split(".")[1]),this._traces.reverse(),t&&(this._runId=t),this._runId&&!this._traces.some((t=>t.run_id===this._runId))){if(this._runId=void 0,this._selected=void 0,t){const t=new URLSearchParams(location.search);t.delete("run_id"),history.replaceState(null,"",`${location.pathname}?${t.toString()}`)}await(0,u.Ys)(this,{text:"Chosen trace is no longer available"})}!this._runId&&this._traces.length>0&&(this._runId=this._traces[0].run_id)}},{kind:"method",key:"_loadTrace",value:async function(){const t=await(0,h.mA)(this.hass,"script",this.scriptEntityId.split(".")[1],this._runId);this._logbookEntries=(0,s.p)(this.hass,"logbook")?await(0,d.sS)(this.hass,t.timestamp.start,t.context.id):[],this._trace=t}},{kind:"method",key:"_downloadTrace",value:function(){const t=document.createElement("a");t.download=`trace ${this.scriptEntityId} ${this._trace.timestamp.start}.json`,t.href=`data:application/json;charset=utf-8,${encodeURI(JSON.stringify({trace:this._trace,logbookEntries:this._logbookEntries},void 0,2))}`,t.click()}},{kind:"method",key:"_importTrace",value:function(){const t=prompt("Enter downloaded trace");t&&(localStorage.devTrace=t,this._loadLocalTrace(t))}},{kind:"method",key:"_loadLocalStorageTrace",value:function(){localStorage.devTrace&&this._loadLocalTrace(localStorage.devTrace)}},{kind:"method",key:"_loadLocalTrace",value:function(t){const e=JSON.parse(t);this._trace=e.trace,this._logbookEntries=e.logbookEntries}},{kind:"method",key:"_showTab",value:function(t){this._view=t.target.view}},{kind:"method",key:"_timelinePathPicked",value:function(t){const e=t.detail.value,i=this._graph.trackedNodes;i[e]&&(this._selected=i[e])}},{kind:"method",key:"_showInfo",value:async function(){this.scriptEntityId&&(0,f.B)(this,"hass-more-info",{entityId:this.scriptEntityId})}},{kind:"get",static:!0,key:"styles",value:function(){return[p.Qx,l.b,r.iv`
        .toolbar {
          display: flex;
          align-items: center;
          justify-content: center;
          height: var(--header-height);
          background-color: var(--primary-background-color);
          color: var(--app-header-text-color, white);
          border-bottom: var(--app-header-border-bottom, none);
          box-sizing: border-box;
        }

        .main {
          height: calc(100% - 56px);
          display: flex;
          background-color: var(--card-background-color);
        }

        :host([narrow]) .main {
          height: auto;
          flex-direction: column;
        }

        .container {
          padding: 16px;
        }

        .graph {
          border-right: 1px solid var(--divider-color);
          overflow-x: auto;
          max-width: 50%;
        }
        :host([narrow]) .graph {
          max-width: 100%;
        }

        .info {
          flex: 1;
          background-color: var(--card-background-color);
        }

        .linkButton {
          color: var(--primary-text-color);
        }
        .trace-link {
          text-decoration: none;
        }
      `]}}]}}),r.oi)}}]);
//# sourceMappingURL=9286c9da.js.map