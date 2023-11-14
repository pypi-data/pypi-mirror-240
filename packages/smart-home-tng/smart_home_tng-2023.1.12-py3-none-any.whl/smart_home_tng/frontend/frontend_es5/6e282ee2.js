"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[16938],{92306:function(e,t,r){r.d(t,{v:function(){return a}});const a=(e,t)=>{const r={};for(const a of e){const e=t(a);e in r?r[e].push(a):r[e]=[a]}return r}},11950:function(e,t,r){r.d(t,{l:function(){return a}});const a=async(e,t)=>new Promise((r=>{const a=t(e,(e=>{a(),r(e)}))}))},81582:function(e,t,r){r.d(t,{LZ:function(){return a},Nn:function(){return l},Ny:function(){return c},Q4:function(){return s},SO:function(){return i},T0:function(){return d},iJ:function(){return o},pB:function(){return n}});const a=32143==r.j?["migration_error","setup_error","setup_retry"]:null,s=32143==r.j?["not_loaded","loaded","setup_error","setup_retry"]:null,n=(e,t)=>{const r={};return t&&(t.type&&(r.type_filter=t.type),t.domain&&(r.domain=t.domain)),e.callWS(Object.assign({type:"config_entries/get"},r))},i=(e,t,r)=>e.callWS(Object.assign({type:"config_entries/update",entry_id:t},r)),o=(e,t)=>e.callApi("DELETE",`config/config_entries/entry/${t}`),l=(e,t)=>e.callApi("POST",`config/config_entries/entry/${t}/reload`),c=(e,t)=>e.callWS({type:"config_entries/disable",entry_id:t,disabled_by:"user"}),d=(e,t)=>e.callWS({type:"config_entries/disable",entry_id:t,disabled_by:null})},55424:function(e,t,r){r.d(t,{Bm:function(){return v},Jj:function(){return W},KU:function(){return C},P:function(){return E},UB:function(){return x},ZC:function(){return T},_Z:function(){return O},_n:function(){return M},gM:function(){return R},gy:function(){return P},iK:function(){return k},jB:function(){return z},o1:function(){return w},rl:function(){return $},vE:function(){return I},vR:function(){return Z},xZ:function(){return S},yH:function(){return K},yT:function(){return F}});var a=r(4535),s=r(59699),n=r(32182),i=r(79021),o=r(39244),l=r(27088),c=r(83008),d=r(70390),u=r(47538),f=r(97330),h=r(92306),_=r(11950),m=r(81582),p=r(74186),y=r(38014);function b(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}const g=[],v=()=>({stat_energy_from:"",stat_cost:null,entity_energy_price:null,number_energy_price:null}),w=()=>({stat_energy_to:"",stat_compensation:null,entity_energy_price:null,number_energy_price:null}),k=()=>({type:"grid",flow_from:[],flow_to:[],cost_adjustment_day:0}),$=()=>({type:"solar",stat_energy_from:"",config_entry_solar_forecast:null}),E=()=>({type:"battery",stat_energy_from:"",stat_energy_to:""}),C=()=>({type:"gas",stat_energy_from:"",stat_cost:null,entity_energy_price:null,number_energy_price:null}),S=e=>e.callWS({type:"energy/info"}),P=e=>e.callWS({type:"energy/validate"});class j extends Error{constructor(e){super(e),b(this,"code","not_found"),Object.setPrototypeOf(this,new.target.prototype)}}const T=async(e,t=!1)=>{const r=await e.callWS({type:"energy/get_prefs"});if(t){const e=r.energy_sources.length>0,t=r.device_consumption.length>0;if(!e&&!t)throw new j}return r},O=async(e,t)=>{const r=e.callWS(Object.assign({type:"energy/save_prefs"},t));return A(e),r},D=async(e,t,r,a,s,n="hour")=>e.callWS({type:"energy/fossil_energy_consumption",start_time:t.toISOString(),end_time:null==s?void 0:s.toISOString(),energy_statistic_ids:r,co2_statistic_id:a,period:n}),W=e=>(0,h.v)(e.energy_sources,(e=>e.type)),K=(e,t)=>{const r=[];for(const a of e.energy_sources)if("solar"!==a.type)if("gas"!==a.type)if("battery"!==a.type){for(const e of a.flow_from){r.push(e.stat_energy_from),e.stat_cost&&r.push(e.stat_cost);const a=t.cost_sensors[e.stat_energy_from];a&&r.push(a)}for(const e of a.flow_to){r.push(e.stat_energy_to),e.stat_compensation&&r.push(e.stat_compensation);const a=t.cost_sensors[e.stat_energy_to];a&&r.push(a)}}else r.push(a.stat_energy_from),r.push(a.stat_energy_to);else{r.push(a.stat_energy_from),a.stat_cost&&r.push(a.stat_cost);const e=t.cost_sensors[a.stat_energy_from];e&&r.push(e)}else r.push(a.stat_energy_from);for(const a of e.device_consumption)r.push(a.stat_consumption);return r},A=e=>{g.forEach((t=>{const r=x(e,{key:t});r.clearPrefs(),r._active&&r.refresh()}))},x=(e,t={})=>{let r="_energy";if(t.key){if(!t.key.startsWith("energy_"))throw new Error("Key need to start with energy_");r=`_${t.key}`}if(e.connection[r])return e.connection[r];g.push(t.key);const h=(0,f._)(e.connection,r,(async()=>{if(h.prefs||(h.prefs=await T(e,!0)),h._refreshTimeout&&clearTimeout(h._refreshTimeout),h._active&&(!h.end||h.end>new Date)){const e=new Date;e.getMinutes()>=20&&e.setHours(e.getHours()+1),e.setMinutes(20,0,0),h._refreshTimeout=window.setTimeout((()=>h.refresh()),e.getTime()-Date.now())}return(async(e,t,r,l,c)=>{const[d,u,f]=await Promise.all([(0,m.pB)(e,{domain:"co2signal"}),(0,_.l)(e.connection,p.LM),S(e)]),h=d.length?d[0]:void 0;let b;if(h)for(const a of u){if(a.config_entry_id!==h.entry_id)continue;const t=e.states[a.entity_id];if(t&&"%"===t.attributes.unit_of_measurement){b=t.entity_id;break}}const g=[];for(const a of t.energy_sources)if("grid"===a.type)for(const e of a.flow_from)g.push(e.stat_energy_from);const v=K(t,f),w=(0,a.Z)(l||new Date,r),k=w>35?"month":w>2?"day":"hour",$=(0,s.Z)(r,-1),E={energy:"kWh",volume:"km"===(e.config.unit_system.length||"")?"m³":"ft³"},C=await(0,y.dL)(e,$,l,v,k,E);let P,j,T,O,W;if(c){j=w>27&&w<32?(0,n.Z)(r,-1):(0,i.Z)(r,-1*(w+1));const t=(0,s.Z)(j,-1);T=(0,o.Z)(r,-1),P=await(0,y.dL)(e,t,T,v,k,E)}void 0!==b&&(O=await D(e,r,g,b,l,w>35?"month":w>2?"day":"hour"),c&&(W=await D(e,j,g,b,T,w>35?"month":w>2?"day":"hour"))),Object.values(C).forEach((e=>{e.length&&new Date(e[0].start)>$&&e.unshift(Object.assign({},e[0],{start:$.toISOString(),end:$.toISOString(),sum:0,state:0}))}));const A=await(0,y.Py)(e,v),x={};return A.forEach((e=>{x[e.statistic_id]=e})),{start:r,end:l,startCompare:j,endCompare:T,info:f,prefs:t,stats:C,statsMetadata:x,statsCompare:P,co2SignalConfigEntry:h,co2SignalEntity:b,fossilEnergyConsumption:O,fossilEnergyConsumptionCompare:W}})(e,h.prefs,h.start,h.end,h.compare)})),b=h.subscribe;h.subscribe=e=>{const t=b(e);return h._active++,()=>{h._active--,h._active<1&&(clearTimeout(h._refreshTimeout),h._refreshTimeout=void 0),t()}},h._active=0,h.prefs=t.prefs;const v=new Date;h.start=v.getHours()>0?(0,l.Z)():(0,c.Z)(),h.end=v.getHours()>0?(0,d.Z)():(0,u.Z)();const w=()=>{h._updatePeriodTimeout=window.setTimeout((()=>{h.start=(0,l.Z)(),h.end=(0,d.Z)(),w()}),(0,s.Z)((0,d.Z)(),1).getTime()-Date.now())};return w(),h.clearPrefs=()=>{h.prefs=void 0},h.setPeriod=(e,t)=>{var r;h.start=e,h.end=t,h.start.getTime()!==(0,l.Z)().getTime()||(null===(r=h.end)||void 0===r?void 0:r.getTime())!==(0,d.Z)().getTime()||h._updatePeriodTimeout?h._updatePeriodTimeout&&(clearTimeout(h._updatePeriodTimeout),h._updatePeriodTimeout=void 0):w()},h.setCompare=e=>{h.compare=e},h},z=e=>e.callWS({type:"energy/solar_forecast"}),R=["m³"],F=["kWh"],M=[...R,...F],Z=(e,t={},r)=>{for(const a of e.energy_sources){if("gas"!==a.type)continue;if(r&&r===a.stat_energy_from)continue;const e=t[a.stat_energy_from];if(e)return R.includes(e.statistics_unit_of_measurement)?"volume":"energy"}},I=(e,t={})=>{for(const r of e.energy_sources){if("gas"!==r.type)continue;const e=t[r.stat_energy_from];if(null!=e&&e.display_unit_of_measurement)return e.display_unit_of_measurement}}},38014:function(e,t,r){r.d(t,{Cj:function(){return l},Kd:function(){return m},Kj:function(){return u},Nw:function(){return h},Py:function(){return n},ZT:function(){return c},dL:function(){return i},hN:function(){return d},h_:function(){return o},j2:function(){return _},q6:function(){return f},uR:function(){return s}});var a=r(91741);const s=(e,t)=>e.callWS({type:"recorder/list_statistic_ids",statistic_type:t}),n=(e,t)=>e.callWS({type:"recorder/get_statistics_metadata",statistic_ids:t}),i=(e,t,r,a,s="hour",n)=>e.callWS({type:"recorder/statistics_during_period",start_time:t.toISOString(),end_time:null==r?void 0:r.toISOString(),statistic_ids:a,period:s,units:n}),o=e=>e.callWS({type:"recorder/validate_statistics"}),l=(e,t,r)=>e.callWS({type:"recorder/update_statistics_metadata",statistic_id:t,unit_of_measurement:r}),c=(e,t,r,a)=>e.callWS({type:"recorder/change_statistics_unit",statistic_id:t,old_unit_of_measurement:r,new_unit_of_measurement:a}),d=(e,t)=>e.callWS({type:"recorder/clear_statistics",statistic_ids:t}),u=e=>{if(!e||e.length<2)return null;const t=e[e.length-1].sum;if(null===t)return null;const r=e[0].sum;return null===r?t:t-r},f=(e,t)=>{let r=null;for(const a of t){if(!(a in e))continue;const t=u(e[a]);null!==t&&(null===r?r=t:r+=t)}return r},h=(e,t)=>e.some((e=>null!==e[t])),_=(e,t,r,a,s)=>e.callWS({type:"recorder/adjust_sum_statistics",statistic_id:t,start_time:r,adjustment:a,display_unit:s}),m=(e,t,r)=>{const s=e.states[t];return s?(0,a.C)(s):(null==r?void 0:r.name)||t}},73826:function(e,t,r){r.d(t,{f:function(){return m}});var a=r(36924);function s(e,t,r,a){var s=n();if(a)for(var d=0;d<a.length;d++)s=a[d](s);var u=t((function(e){s.initializeInstanceElements(e,f.elements)}),r),f=s.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},a=0;a<e.length;a++){var s,n=e[a];if("method"===n.kind&&(s=t.find(r)))if(c(n.descriptor)||c(s.descriptor)){if(l(n)||l(s))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");s.descriptor=n.descriptor}else{if(l(n)){if(l(s))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");s.decorators=n.decorators}o(n,s)}else t.push(n)}return t}(u.d.map(i)),e);return s.initializeClassElements(u.F,f.elements),s.runClassFinishers(u.F,f.finishers)}function n(){n=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(a){t.forEach((function(t){var s=t.placement;if(t.kind===a&&("static"===s||"prototype"===s)){var n="static"===s?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var a=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===a?void 0:a.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],a=[],s={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,s)}),this),e.forEach((function(e){if(!l(e))return r.push(e);var t=this.decorateElement(e,s);r.push(t.element),r.push.apply(r,t.extras),a.push.apply(a,t.finishers)}),this),!t)return{elements:r,finishers:a};var n=this.decorateConstructor(r,t);return a.push.apply(a,n.finishers),n.finishers=a,n},addElementPlacement:function(e,t,r){var a=t[e.placement];if(!r&&-1!==a.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");a.push(e.key)},decorateElement:function(e,t){for(var r=[],a=[],s=e.decorators,n=s.length-1;n>=0;n--){var i=t[e.placement];i.splice(i.indexOf(e.key),1);var o=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,s[n])(o)||o);e=l.element,this.addElementPlacement(e,t),l.finisher&&a.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:a,extras:r}},decorateConstructor:function(e,t){for(var r=[],a=t.length-1;a>=0;a--){var s=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[a])(s)||s);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var i=0;i<e.length-1;i++)for(var o=i+1;o<e.length;o++)if(e[i].key===e[o].key&&e[i].placement===e[o].placement)throw new TypeError("Duplicated element ("+e[i].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?f(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),a=String(e.placement);if("static"!==a&&"prototype"!==a&&"own"!==a)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+a+'"');var s=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:a,descriptor:Object.assign({},s)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(s,"get","The property descriptor of a field descriptor"),this.disallowProperty(s,"set","The property descriptor of a field descriptor"),this.disallowProperty(s,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var a=(0,t[r])(e);if(void 0!==a){if("function"!=typeof a)throw new TypeError("Finishers must return a constructor.");e=a}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function i(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var a={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(a.decorators=e.decorators),"field"===e.kind&&(a.initializer=e.value),a}function o(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function l(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}function h(){return h="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var a=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=_(e)););return e}(e,t);if(a){var s=Object.getOwnPropertyDescriptor(a,t);return s.get?s.get.call(arguments.length<3?e:r):s.value}},h.apply(this,arguments)}function _(e){return _=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},_(e)}const m=e=>s(null,(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){h(_(r.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if(h(_(r.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){const e=this.__unsubs.pop();e instanceof Promise?e.then((e=>e())):e()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(e){if(h(_(r.prototype),"updated",this).call(this,e),e.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps)for(const t of e.keys())if(this.hassSubscribeRequiredHostProps.includes(t))return void this.__checkSubscribed()}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var e;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(e=this.hassSubscribeRequiredHostProps)&&void 0!==e&&e.some((e=>void 0===this[e]))||(this.__unsubs=this.hassSubscribe())}}]}}),e)},16938:function(e,t,r){r.r(t),r.d(t,{HuiEnergySourcesTableCard:function(){return w}});var a=r(40521),s=r(37500),n=r(36924),i=r(70483),o=r(15838),l=r(89525),c=r(18457),d=(r(22098),r(55424)),u=r(38014),f=r(73826);function h(){h=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(a){t.forEach((function(t){var s=t.placement;if(t.kind===a&&("static"===s||"prototype"===s)){var n="static"===s?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var a=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===a?void 0:a.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],a=[],s={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,s)}),this),e.forEach((function(e){if(!p(e))return r.push(e);var t=this.decorateElement(e,s);r.push(t.element),r.push.apply(r,t.extras),a.push.apply(a,t.finishers)}),this),!t)return{elements:r,finishers:a};var n=this.decorateConstructor(r,t);return a.push.apply(a,n.finishers),n.finishers=a,n},addElementPlacement:function(e,t,r){var a=t[e.placement];if(!r&&-1!==a.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");a.push(e.key)},decorateElement:function(e,t){for(var r=[],a=[],s=e.decorators,n=s.length-1;n>=0;n--){var i=t[e.placement];i.splice(i.indexOf(e.key),1);var o=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,s[n])(o)||o);e=l.element,this.addElementPlacement(e,t),l.finisher&&a.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:a,extras:r}},decorateConstructor:function(e,t){for(var r=[],a=t.length-1;a>=0;a--){var s=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[a])(s)||s);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var i=0;i<e.length-1;i++)for(var o=i+1;o<e.length;o++)if(e[i].key===e[o].key&&e[i].placement===e[o].placement)throw new TypeError("Duplicated element ("+e[i].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return v(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?v(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=g(e.key),a=String(e.placement);if("static"!==a&&"prototype"!==a&&"own"!==a)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+a+'"');var s=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:a,descriptor:Object.assign({},s)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(s,"get","The property descriptor of a field descriptor"),this.disallowProperty(s,"set","The property descriptor of a field descriptor"),this.disallowProperty(s,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:b(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=b(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var a=(0,t[r])(e);if(void 0!==a){if("function"!=typeof a)throw new TypeError("Finishers must return a constructor.");e=a}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function _(e){var t,r=g(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var a={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(a.decorators=e.decorators),"field"===e.kind&&(a.initializer=e.value),a}function m(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function p(e){return e.decorators&&e.decorators.length}function y(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function b(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function g(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function v(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}let w=function(e,t,r,a){var s=h();if(a)for(var n=0;n<a.length;n++)s=a[n](s);var i=t((function(e){s.initializeInstanceElements(e,o.elements)}),r),o=s.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},a=0;a<e.length;a++){var s,n=e[a];if("method"===n.kind&&(s=t.find(r)))if(y(n.descriptor)||y(s.descriptor)){if(p(n)||p(s))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");s.descriptor=n.descriptor}else{if(p(n)){if(p(s))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");s.decorators=n.decorators}m(n,s)}else t.push(n)}return t}(i.d.map(_)),e);return s.initializeClassElements(i.F,o.elements),s.runClassFinishers(i.F,o.finishers)}([(0,n.Mo)("hui-energy-sources-table-card")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return["_config"]}},{kind:"method",key:"hassSubscribe",value:function(){var e;return[(0,d.UB)(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((e=>{this._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"render",value:function(){var e,t,r,a,n,f,h;if(!this.hass||!this._config)return s.dy``;if(!this._data)return s.dy`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;let _=0,m=0,p=0,y=0,b=0,g=0,v=0,w=0,k=0,$=0,E=0,C=0;const S=(0,d.Jj)(this._data.prefs),P=getComputedStyle(this),j=P.getPropertyValue("--energy-solar-color").trim(),T=P.getPropertyValue("--energy-battery-out-color").trim(),O=P.getPropertyValue("--energy-battery-in-color").trim(),D=P.getPropertyValue("--energy-grid-return-color").trim(),W=P.getPropertyValue("--energy-grid-consumption-color").trim(),K=P.getPropertyValue("--energy-gas-color").trim(),A=(null===(e=S.grid)||void 0===e?void 0:e[0].flow_from.some((e=>e.stat_cost||e.entity_energy_price||e.number_energy_price)))||(null===(t=S.grid)||void 0===t?void 0:t[0].flow_to.some((e=>e.stat_compensation||e.entity_energy_price||e.number_energy_price)))||(null===(r=S.gas)||void 0===r?void 0:r.some((e=>e.stat_cost||e.entity_energy_price||e.number_energy_price))),x=(0,d.vE)(this._data.prefs,this._data.statsMetadata)||"",z=void 0!==this._data.statsCompare;return s.dy` <ha-card>
      ${this._config.title?s.dy`<h1 class="card-header">${this._config.title}</h1>`:""}
      <div class="mdc-data-table">
        <div class="mdc-data-table__table-container">
          <table class="mdc-data-table__table" aria-label="Energy sources">
            <thead>
              <tr class="mdc-data-table__header-row">
                <th class="mdc-data-table__header-cell"></th>
                <th
                  class="mdc-data-table__header-cell"
                  role="columnheader"
                  scope="col"
                >
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.source")}
                </th>
                ${z?s.dy`<th
                        class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric"
                        role="columnheader"
                        scope="col"
                      >
                        ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.previous_energy")}
                      </th>
                      ${A?s.dy`<th
                            class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric"
                            role="columnheader"
                            scope="col"
                          >
                            ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.previous_cost")}
                          </th>`:""}`:""}
                <th
                  class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric"
                  role="columnheader"
                  scope="col"
                >
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.energy")}
                </th>
                ${A?s.dy` <th
                      class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric"
                      role="columnheader"
                      scope="col"
                    >
                      ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.cost")}
                    </th>`:""}
              </tr>
            </thead>
            <tbody class="mdc-data-table__content">
              ${null===(a=S.solar)||void 0===a?void 0:a.map(((e,t)=>{var r;const a=(0,u.Kj)(this._data.stats[e.stat_energy_from])||0;p+=a;const n=z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_from])||0;k+=n;const d=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(j)),t):(0,l.W)((0,o.Rw)((0,o.wK)(j)),t):void 0,f=d?(0,o.CO)((0,o.p3)(d)):j;return s.dy`<tr class="mdc-data-table__row">
                  <td class="mdc-data-table__cell cell-bullet">
                    <div
                      class="bullet"
                      style=${(0,i.V)({borderColor:f,backgroundColor:f+"7F"})}
                    ></div>
                  </td>
                  <th class="mdc-data-table__cell" scope="row">
                    ${(0,u.Kd)(this.hass,e.stat_energy_from,null===(r=this._data)||void 0===r?void 0:r.statsMetadata[e.stat_energy_from])}
                  </th>
                  ${z?s.dy`<td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${(0,c.uf)(n,this.hass.locale)} kWh
                        </td>
                        ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}`:""}
                  <td
                    class="mdc-data-table__cell mdc-data-table__cell--numeric"
                  >
                    ${(0,c.uf)(a,this.hass.locale)} kWh
                  </td>
                  ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                </tr>`}))}
              ${S.solar?s.dy`<tr class="mdc-data-table__row total">
                    <td class="mdc-data-table__cell"></td>
                    <th class="mdc-data-table__cell" scope="row">
                      Solar total
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(k,this.hass.locale)}
                            kWh
                          </td>
                          ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(p,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                  </tr>`:""}
              ${null===(n=S.battery)||void 0===n?void 0:n.map(((e,t)=>{var r,a;const n=(0,u.Kj)(this._data.stats[e.stat_energy_from])||0,d=(0,u.Kj)(this._data.stats[e.stat_energy_to])||0;y+=n-d;const f=z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_from])||0,h=z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_to])||0;$+=f-h;const _=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(T)),t):(0,l.W)((0,o.Rw)((0,o.wK)(T)),t):void 0,m=_?(0,o.CO)((0,o.p3)(_)):T,p=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(O)),t):(0,l.W)((0,o.Rw)((0,o.wK)(O)),t):void 0,b=p?(0,o.CO)((0,o.p3)(p)):O;return s.dy`<tr class="mdc-data-table__row">
                    <td class="mdc-data-table__cell cell-bullet">
                      <div
                        class="bullet"
                        style=${(0,i.V)({borderColor:m,backgroundColor:m+"7F"})}
                      ></div>
                    </td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${(0,u.Kd)(this.hass,e.stat_energy_from,null===(r=this._data)||void 0===r?void 0:r.statsMetadata[e.stat_energy_from])}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(f,this.hass.locale)}
                            kWh
                          </td>
                          ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(n,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                  </tr>
                  <tr class="mdc-data-table__row">
                    <td class="mdc-data-table__cell cell-bullet">
                      <div
                        class="bullet"
                        style=${(0,i.V)({borderColor:b,backgroundColor:b+"7F"})}
                      ></div>
                    </td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${(0,u.Kd)(this.hass,e.stat_energy_to,null===(a=this._data)||void 0===a?void 0:a.statsMetadata[e.stat_energy_to])}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(-1*h,this.hass.locale)}
                            kWh
                          </td>
                          ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(-1*d,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                  </tr>`}))}
              ${S.battery?s.dy`<tr class="mdc-data-table__row total">
                    <td class="mdc-data-table__cell"></td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.battery_total")}
                    </th>
                    ${z?s.dy` <td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)($,this.hass.locale)}
                            kWh
                          </td>
                          ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(y,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                  </tr>`:""}
              ${null===(f=S.grid)||void 0===f?void 0:f.map((e=>s.dy`${e.flow_from.map(((e,t)=>{var r;const a=(0,u.Kj)(this._data.stats[e.stat_energy_from])||0;_+=a;const n=z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_from])||0;v+=n;const d=e.stat_cost||this._data.info.cost_sensors[e.stat_energy_from],f=d?(0,u.Kj)(this._data.stats[d])||0:null;null!==f&&(m+=f);const h=z&&d?(0,u.Kj)(this._data.statsCompare[d])||0:null;null!==h&&(w+=h);const p=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(W)),t):(0,l.W)((0,o.Rw)((0,o.wK)(W)),t):void 0,y=p?(0,o.CO)((0,o.p3)(p)):W;return s.dy`<tr class="mdc-data-table__row">
                    <td class="mdc-data-table__cell cell-bullet">
                      <div
                        class="bullet"
                        style=${(0,i.V)({borderColor:y,backgroundColor:y+"7F"})}
                      ></div>
                    </td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${(0,u.Kd)(this.hass,e.stat_energy_from,null===(r=this._data)||void 0===r?void 0:r.statsMetadata[e.stat_energy_from])}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(n,this.hass.locale)} kWh
                          </td>
                          ${A?s.dy`<td
                                class="mdc-data-table__cell mdc-data-table__cell--numeric"
                              >
                                ${null!==h?(0,c.uf)(h,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                              </td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(a,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy` <td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${null!==f?(0,c.uf)(f,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                        </td>`:""}
                  </tr>`}))}
                ${e.flow_to.map(((e,t)=>{var r;const a=-1*((0,u.Kj)(this._data.stats[e.stat_energy_to])||0);_+=a;const n=e.stat_compensation||this._data.info.cost_sensors[e.stat_energy_to],d=n?-1*((0,u.Kj)(this._data.stats[n])||0):null;null!==d&&(m+=d);const f=-1*(z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_to])||0);v+=f;const h=z&&n?-1*((0,u.Kj)(this._data.statsCompare[n])||0):null;null!==h&&(w+=h);const p=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(D)),t):(0,l.W)((0,o.Rw)((0,o.wK)(D)),t):void 0,y=p?(0,o.CO)((0,o.p3)(p)):D;return s.dy`<tr class="mdc-data-table__row">
                    <td class="mdc-data-table__cell cell-bullet">
                      <div
                        class="bullet"
                        style=${(0,i.V)({borderColor:y,backgroundColor:y+"7F"})}
                      ></div>
                    </td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${(0,u.Kd)(this.hass,e.stat_energy_to,null===(r=this._data)||void 0===r?void 0:r.statsMetadata[e.stat_energy_to])}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(f,this.hass.locale)} kWh
                          </td>
                          ${A?s.dy`<td
                                class="mdc-data-table__cell mdc-data-table__cell--numeric"
                              >
                                ${null!==h?(0,c.uf)(h,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                              </td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(a,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy` <td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${null!==d?(0,c.uf)(d,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                        </td>`:""}
                  </tr>`}))}`))}
              ${S.grid?s.dy` <tr class="mdc-data-table__row total">
                    <td class="mdc-data-table__cell"></td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.grid_total")}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(v,this.hass.locale)}
                            kWh
                          </td>
                          ${A?s.dy`<td
                                class="mdc-data-table__cell mdc-data-table__cell--numeric"
                              >
                                ${(0,c.uf)(w,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                              </td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(_,this.hass.locale)} kWh
                    </td>
                    ${A?s.dy`<td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${(0,c.uf)(m,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                        </td>`:""}
                  </tr>`:""}
              ${null===(h=S.gas)||void 0===h?void 0:h.map(((e,t)=>{var r;const a=(0,u.Kj)(this._data.stats[e.stat_energy_from])||0;b+=a;const n=z&&(0,u.Kj)(this._data.statsCompare[e.stat_energy_from])||0;E+=n;const d=e.stat_cost||this._data.info.cost_sensors[e.stat_energy_from],f=d?(0,u.Kj)(this._data.stats[d])||0:null;null!==f&&(g+=f);const h=z&&d?(0,u.Kj)(this._data.statsCompare[d])||0:null;null!==h&&(C+=h);const _=t>0?this.hass.themes.darkMode?(0,l.C)((0,o.Rw)((0,o.wK)(K)),t):(0,l.W)((0,o.Rw)((0,o.wK)(K)),t):void 0,m=_?(0,o.CO)((0,o.p3)(_)):K;return s.dy`<tr class="mdc-data-table__row">
                  <td class="mdc-data-table__cell cell-bullet">
                    <div
                      class="bullet"
                      style=${(0,i.V)({borderColor:m,backgroundColor:m+"7F"})}
                    ></div>
                  </td>
                  <th class="mdc-data-table__cell" scope="row">
                    ${(0,u.Kd)(this.hass,e.stat_energy_from,null===(r=this._data)||void 0===r?void 0:r.statsMetadata[e.stat_energy_from])}
                  </th>
                  ${z?s.dy` <td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${(0,c.uf)(n,this.hass.locale)}
                          ${x}
                        </td>
                        ${A?s.dy`<td
                              class="mdc-data-table__cell mdc-data-table__cell--numeric"
                            >
                              ${null!==h?(0,c.uf)(h,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                            </td>`:""}`:""}
                  <td
                    class="mdc-data-table__cell mdc-data-table__cell--numeric"
                  >
                    ${(0,c.uf)(a,this.hass.locale)} ${x}
                  </td>
                  ${A?s.dy`<td
                        class="mdc-data-table__cell mdc-data-table__cell--numeric"
                      >
                        ${null!==f?(0,c.uf)(f,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""}
                      </td>`:""}
                </tr>`}))}
              ${S.gas?s.dy`<tr class="mdc-data-table__row total">
                    <td class="mdc-data-table__cell"></td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.gas_total")}
                    </th>
                    ${z?s.dy`<td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(E,this.hass.locale)}
                            ${x}
                          </td>
                          ${A?s.dy`<td
                                class="mdc-data-table__cell mdc-data-table__cell--numeric"
                              >
                                ${(0,c.uf)(C,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                              </td>`:""}`:""}
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(b,this.hass.locale)} ${x}
                    </td>
                    ${A?s.dy`<td
                          class="mdc-data-table__cell mdc-data-table__cell--numeric"
                        >
                          ${(0,c.uf)(g,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                        </td>`:""}
                  </tr>`:""}
              ${g&&m?s.dy`<tr class="mdc-data-table__row total">
                    <td class="mdc-data-table__cell"></td>
                    <th class="mdc-data-table__cell" scope="row">
                      ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.total_costs")}
                    </th>
                    ${z?s.dy`${A?s.dy`<td class="mdc-data-table__cell"></td>`:""}
                          <td
                            class="mdc-data-table__cell mdc-data-table__cell--numeric"
                          >
                            ${(0,c.uf)(C+w,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                          </td>`:""}
                    <td class="mdc-data-table__cell"></td>
                    <td
                      class="mdc-data-table__cell mdc-data-table__cell--numeric"
                    >
                      ${(0,c.uf)(g+m,this.hass.locale,{style:"currency",currency:this.hass.config.currency})}
                    </td>
                  </tr>`:""}
            </tbody>
          </table>
        </div>
      </div>
    </ha-card>`}},{kind:"get",static:!0,key:"styles",value:function(){return s.iv`
      ${(0,s.$m)(a)}
      .mdc-data-table {
        width: 100%;
        border: 0;
      }
      .mdc-data-table__header-cell,
      .mdc-data-table__cell {
        color: var(--primary-text-color);
        border-bottom-color: var(--divider-color);
        text-align: var(--float-start);
      }
      .mdc-data-table__row:not(.mdc-data-table__row--selected):hover {
        background-color: rgba(var(--rgb-primary-text-color), 0.04);
      }
      .total {
        --mdc-typography-body2-font-weight: 500;
      }
      .total .mdc-data-table__cell {
        border-top: 1px solid var(--divider-color);
      }
      ha-card {
        height: 100%;
      }
      .card-header {
        padding-bottom: 0;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
      .cell-bullet {
        width: 32px;
        padding-right: 0;
        padding-inline-end: 0;
        padding-inline-start: 16px;
        direction: var(--direction);
      }
      .bullet {
        border-width: 1px;
        border-style: solid;
        border-radius: 4px;
        height: 16px;
        width: 32px;
      }
      .mdc-data-table__cell--numeric {
        direction: ltr;
      }
    `}}]}}),(0,f.f)(s.oi))}}]);
//# sourceMappingURL=6e282ee2.js.map