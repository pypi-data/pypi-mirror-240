"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[9928],{23682:function(e,t,r){function n(e,t){if(t.length<e)throw new TypeError(e+" argument"+(e>1?"s":"")+" required, but only "+t.length+" present")}r.d(t,{Z:function(){return n}})},90394:function(e,t,r){function n(e){if(null===e||!0===e||!1===e)return NaN;var t=Number(e);return isNaN(t)?t:t<0?Math.ceil(t):Math.floor(t)}r.d(t,{Z:function(){return n}})},79021:function(e,t,r){r.d(t,{Z:function(){return s}});var n=r(90394),i=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,i.Z)(e),s=(0,n.Z)(t);return isNaN(s)?new Date(NaN):s?(r.setDate(r.getDate()+s),r):r}},59699:function(e,t,r){r.d(t,{Z:function(){return a}});var n=r(90394),i=r(39244),o=r(23682),s=36e5;function a(e,t){(0,o.Z)(2,arguments);var r=(0,n.Z)(t);return(0,i.Z)(e,r*s)}},39244:function(e,t,r){r.d(t,{Z:function(){return s}});var n=r(90394),i=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,i.Z)(e).getTime(),s=(0,n.Z)(t);return new Date(r+s)}},32182:function(e,t,r){r.d(t,{Z:function(){return s}});var n=r(90394),i=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,i.Z)(e),s=(0,n.Z)(t);if(isNaN(s))return new Date(NaN);if(!s)return r;var a=r.getDate(),c=new Date(r.getTime());return c.setMonth(r.getMonth()+s+1,0),a>=c.getDate()?c:(r.setFullYear(c.getFullYear(),c.getMonth(),a),r)}},4535:function(e,t,r){r.d(t,{Z:function(){return l}});var n=r(34327);function i(e){var t=new Date(Date.UTC(e.getFullYear(),e.getMonth(),e.getDate(),e.getHours(),e.getMinutes(),e.getSeconds(),e.getMilliseconds()));return t.setUTCFullYear(e.getFullYear()),e.getTime()-t.getTime()}var o=r(59429),s=r(23682),a=864e5;function c(e,t){var r=e.getFullYear()-t.getFullYear()||e.getMonth()-t.getMonth()||e.getDate()-t.getDate()||e.getHours()-t.getHours()||e.getMinutes()-t.getMinutes()||e.getSeconds()-t.getSeconds()||e.getMilliseconds()-t.getMilliseconds();return r<0?-1:r>0?1:r}function l(e,t){(0,s.Z)(2,arguments);var r=(0,n.Z)(e),l=(0,n.Z)(t),u=c(r,l),d=Math.abs(function(e,t){(0,s.Z)(2,arguments);var r=(0,o.Z)(e),n=(0,o.Z)(t),c=r.getTime()-i(r),l=n.getTime()-i(n);return Math.round((c-l)/a)}(r,l));r.setDate(r.getDate()-u*d);var f=u*(d-Number(c(r,l)===-u));return 0===f?0:f}},93752:function(e,t,r){r.d(t,{Z:function(){return o}});var n=r(34327),i=r(23682);function o(e){(0,i.Z)(1,arguments);var t=(0,n.Z)(e);return t.setHours(23,59,59,999),t}},70390:function(e,t,r){r.d(t,{Z:function(){return i}});var n=r(93752);function i(){return(0,n.Z)(Date.now())}},47538:function(e,t,r){function n(){var e=new Date,t=e.getFullYear(),r=e.getMonth(),n=e.getDate(),i=new Date(0);return i.setFullYear(t,r,n-1),i.setHours(23,59,59,999),i}r.d(t,{Z:function(){return n}})},59429:function(e,t,r){r.d(t,{Z:function(){return o}});var n=r(34327),i=r(23682);function o(e){(0,i.Z)(1,arguments);var t=(0,n.Z)(e);return t.setHours(0,0,0,0),t}},27088:function(e,t,r){r.d(t,{Z:function(){return i}});var n=r(59429);function i(){return(0,n.Z)(Date.now())}},83008:function(e,t,r){function n(){var e=new Date,t=e.getFullYear(),r=e.getMonth(),n=e.getDate(),i=new Date(0);return i.setFullYear(t,r,n-1),i.setHours(0,0,0,0),i}r.d(t,{Z:function(){return n}})},34327:function(e,t,r){r.d(t,{Z:function(){return o}});var n=r(76775),i=r(23682);function o(e){(0,i.Z)(1,arguments);var t=Object.prototype.toString.call(e);return e instanceof Date||"object"===(0,n.Z)(e)&&"[object Date]"===t?new Date(e.getTime()):"number"==typeof e||"[object Number]"===t?new Date(e):("string"!=typeof e&&"[object String]"!==t||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments"),console.warn((new Error).stack)),new Date(NaN))}},92306:function(e,t,r){r.d(t,{v:function(){return n}});const n=(e,t)=>{const r={};for(const n of e){const e=t(n);e in r?r[e].push(n):r[e]=[n]}return r}},11950:function(e,t,r){r.d(t,{l:function(){return n}});const n=async(e,t)=>new Promise((r=>{const n=t(e,(e=>{n(),r(e)}))}))},81582:function(e,t,r){r.d(t,{LZ:function(){return n},Nn:function(){return c},Ny:function(){return l},Q4:function(){return i},SO:function(){return s},T0:function(){return u},iJ:function(){return a},pB:function(){return o}});const n=32143==r.j?["migration_error","setup_error","setup_retry"]:null,i=32143==r.j?["not_loaded","loaded","setup_error","setup_retry"]:null,o=(e,t)=>{const r={};return t&&(t.type&&(r.type_filter=t.type),t.domain&&(r.domain=t.domain)),e.callWS(Object.assign({type:"config_entries/get"},r))},s=(e,t,r)=>e.callWS(Object.assign({type:"config_entries/update",entry_id:t},r)),a=(e,t)=>e.callApi("DELETE",`config/config_entries/entry/${t}`),c=(e,t)=>e.callApi("POST",`config/config_entries/entry/${t}/reload`),l=(e,t)=>e.callWS({type:"config_entries/disable",entry_id:t,disabled_by:"user"}),u=(e,t)=>e.callWS({type:"config_entries/disable",entry_id:t,disabled_by:null})},55424:function(e,t,r){r.d(t,{Bm:function(){return _},Jj:function(){return Z},KU:function(){return x},P:function(){return C},UB:function(){return j},ZC:function(){return M},_Z:function(){return D},_n:function(){return F},gM:function(){return A},gy:function(){return P},iK:function(){return w},jB:function(){return O},o1:function(){return k},rl:function(){return E},vE:function(){return Y},vR:function(){return W},xZ:function(){return S},yH:function(){return T},yT:function(){return z}});var n=r(4535),i=r(59699),o=r(32182),s=r(79021),a=r(39244),c=r(27088),l=r(83008),u=r(70390),d=r(47538),f=r(97330),p=r(92306),h=r(11950),y=r(81582),m=r(74186),g=r(38014);function v(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}const b=[],_=()=>({stat_energy_from:"",stat_cost:null,entity_energy_price:null,number_energy_price:null}),k=()=>({stat_energy_to:"",stat_compensation:null,entity_energy_price:null,number_energy_price:null}),w=()=>({type:"grid",flow_from:[],flow_to:[],cost_adjustment_day:0}),E=()=>({type:"solar",stat_energy_from:"",config_entry_solar_forecast:null}),C=()=>({type:"battery",stat_energy_from:"",stat_energy_to:""}),x=()=>({type:"gas",stat_energy_from:"",stat_cost:null,entity_energy_price:null,number_energy_price:null}),S=e=>e.callWS({type:"energy/info"}),P=e=>e.callWS({type:"energy/validate"});class $ extends Error{constructor(e){super(e),v(this,"code","not_found"),Object.setPrototypeOf(this,new.target.prototype)}}const M=async(e,t=!1)=>{const r=await e.callWS({type:"energy/get_prefs"});if(t){const e=r.energy_sources.length>0,t=r.device_consumption.length>0;if(!e&&!t)throw new $}return r},D=async(e,t)=>{const r=e.callWS(Object.assign({type:"energy/save_prefs"},t));return H(e),r},L=async(e,t,r,n,i,o="hour")=>e.callWS({type:"energy/fossil_energy_consumption",start_time:t.toISOString(),end_time:null==i?void 0:i.toISOString(),energy_statistic_ids:r,co2_statistic_id:n,period:o}),Z=e=>(0,p.v)(e.energy_sources,(e=>e.type)),T=(e,t)=>{const r=[];for(const n of e.energy_sources)if("solar"!==n.type)if("gas"!==n.type)if("battery"!==n.type){for(const e of n.flow_from){r.push(e.stat_energy_from),e.stat_cost&&r.push(e.stat_cost);const n=t.cost_sensors[e.stat_energy_from];n&&r.push(n)}for(const e of n.flow_to){r.push(e.stat_energy_to),e.stat_compensation&&r.push(e.stat_compensation);const n=t.cost_sensors[e.stat_energy_to];n&&r.push(n)}}else r.push(n.stat_energy_from),r.push(n.stat_energy_to);else{r.push(n.stat_energy_from),n.stat_cost&&r.push(n.stat_cost);const e=t.cost_sensors[n.stat_energy_from];e&&r.push(e)}else r.push(n.stat_energy_from);for(const n of e.device_consumption)r.push(n.stat_consumption);return r},H=e=>{b.forEach((t=>{const r=j(e,{key:t});r.clearPrefs(),r._active&&r.refresh()}))},j=(e,t={})=>{let r="_energy";if(t.key){if(!t.key.startsWith("energy_"))throw new Error("Key need to start with energy_");r=`_${t.key}`}if(e.connection[r])return e.connection[r];b.push(t.key);const p=(0,f._)(e.connection,r,(async()=>{if(p.prefs||(p.prefs=await M(e,!0)),p._refreshTimeout&&clearTimeout(p._refreshTimeout),p._active&&(!p.end||p.end>new Date)){const e=new Date;e.getMinutes()>=20&&e.setHours(e.getHours()+1),e.setMinutes(20,0,0),p._refreshTimeout=window.setTimeout((()=>p.refresh()),e.getTime()-Date.now())}return(async(e,t,r,c,l)=>{const[u,d,f]=await Promise.all([(0,y.pB)(e,{domain:"co2signal"}),(0,h.l)(e.connection,m.LM),S(e)]),p=u.length?u[0]:void 0;let v;if(p)for(const n of d){if(n.config_entry_id!==p.entry_id)continue;const t=e.states[n.entity_id];if(t&&"%"===t.attributes.unit_of_measurement){v=t.entity_id;break}}const b=[];for(const n of t.energy_sources)if("grid"===n.type)for(const e of n.flow_from)b.push(e.stat_energy_from);const _=T(t,f),k=(0,n.Z)(c||new Date,r),w=k>35?"month":k>2?"day":"hour",E=(0,i.Z)(r,-1),C={energy:"kWh",volume:"km"===(e.config.unit_system.length||"")?"m³":"ft³"},x=await(0,g.dL)(e,E,c,_,w,C);let P,$,M,D,Z;if(l){$=k>27&&k<32?(0,o.Z)(r,-1):(0,s.Z)(r,-1*(k+1));const t=(0,i.Z)($,-1);M=(0,a.Z)(r,-1),P=await(0,g.dL)(e,t,M,_,w,C)}void 0!==v&&(D=await L(e,r,b,v,c,k>35?"month":k>2?"day":"hour"),l&&(Z=await L(e,$,b,v,M,k>35?"month":k>2?"day":"hour"))),Object.values(x).forEach((e=>{e.length&&new Date(e[0].start)>E&&e.unshift(Object.assign({},e[0],{start:E.toISOString(),end:E.toISOString(),sum:0,state:0}))}));const H=await(0,g.Py)(e,_),j={};return H.forEach((e=>{j[e.statistic_id]=e})),{start:r,end:c,startCompare:$,endCompare:M,info:f,prefs:t,stats:x,statsMetadata:j,statsCompare:P,co2SignalConfigEntry:p,co2SignalEntity:v,fossilEnergyConsumption:D,fossilEnergyConsumptionCompare:Z}})(e,p.prefs,p.start,p.end,p.compare)})),v=p.subscribe;p.subscribe=e=>{const t=v(e);return p._active++,()=>{p._active--,p._active<1&&(clearTimeout(p._refreshTimeout),p._refreshTimeout=void 0),t()}},p._active=0,p.prefs=t.prefs;const _=new Date;p.start=_.getHours()>0?(0,c.Z)():(0,l.Z)(),p.end=_.getHours()>0?(0,u.Z)():(0,d.Z)();const k=()=>{p._updatePeriodTimeout=window.setTimeout((()=>{p.start=(0,c.Z)(),p.end=(0,u.Z)(),k()}),(0,i.Z)((0,u.Z)(),1).getTime()-Date.now())};return k(),p.clearPrefs=()=>{p.prefs=void 0},p.setPeriod=(e,t)=>{var r;p.start=e,p.end=t,p.start.getTime()!==(0,c.Z)().getTime()||(null===(r=p.end)||void 0===r?void 0:r.getTime())!==(0,u.Z)().getTime()||p._updatePeriodTimeout?p._updatePeriodTimeout&&(clearTimeout(p._updatePeriodTimeout),p._updatePeriodTimeout=void 0):k()},p.setCompare=e=>{p.compare=e},p},O=e=>e.callWS({type:"energy/solar_forecast"}),A=["m³"],z=["kWh"],F=[...A,...z],W=(e,t={},r)=>{for(const n of e.energy_sources){if("gas"!==n.type)continue;if(r&&r===n.stat_energy_from)continue;const e=t[n.stat_energy_from];if(e)return A.includes(e.statistics_unit_of_measurement)?"volume":"energy"}},Y=(e,t={})=>{for(const r of e.energy_sources){if("gas"!==r.type)continue;const e=t[r.stat_energy_from];if(null!=e&&e.display_unit_of_measurement)return e.display_unit_of_measurement}}},38014:function(e,t,r){r.d(t,{Cj:function(){return c},Kd:function(){return y},Kj:function(){return d},Nw:function(){return p},Py:function(){return o},ZT:function(){return l},dL:function(){return s},hN:function(){return u},h_:function(){return a},j2:function(){return h},q6:function(){return f},uR:function(){return i}});var n=r(91741);const i=(e,t)=>e.callWS({type:"recorder/list_statistic_ids",statistic_type:t}),o=(e,t)=>e.callWS({type:"recorder/get_statistics_metadata",statistic_ids:t}),s=(e,t,r,n,i="hour",o)=>e.callWS({type:"recorder/statistics_during_period",start_time:t.toISOString(),end_time:null==r?void 0:r.toISOString(),statistic_ids:n,period:i,units:o}),a=e=>e.callWS({type:"recorder/validate_statistics"}),c=(e,t,r)=>e.callWS({type:"recorder/update_statistics_metadata",statistic_id:t,unit_of_measurement:r}),l=(e,t,r,n)=>e.callWS({type:"recorder/change_statistics_unit",statistic_id:t,old_unit_of_measurement:r,new_unit_of_measurement:n}),u=(e,t)=>e.callWS({type:"recorder/clear_statistics",statistic_ids:t}),d=e=>{if(!e||e.length<2)return null;const t=e[e.length-1].sum;if(null===t)return null;const r=e[0].sum;return null===r?t:t-r},f=(e,t)=>{let r=null;for(const n of t){if(!(n in e))continue;const t=d(e[n]);null!==t&&(null===r?r=t:r+=t)}return r},p=(e,t)=>e.some((e=>null!==e[t])),h=(e,t,r,n,i)=>e.callWS({type:"recorder/adjust_sum_statistics",statistic_id:t,start_time:r,adjustment:n,display_unit:i}),y=(e,t,r)=>{const i=e.states[t];return i?(0,n.C)(i):(null==r?void 0:r.name)||t}},73826:function(e,t,r){r.d(t,{f:function(){return y}});var n=r(36924);function i(e,t,r,n){var i=o();if(n)for(var u=0;u<n.length;u++)i=n[u](i);var d=t((function(e){i.initializeInstanceElements(e,f.elements)}),r),f=i.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},n=0;n<e.length;n++){var i,o=e[n];if("method"===o.kind&&(i=t.find(r)))if(l(o.descriptor)||l(i.descriptor)){if(c(o)||c(i))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");i.descriptor=o.descriptor}else{if(c(o)){if(c(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");i.decorators=o.decorators}a(o,i)}else t.push(o)}return t}(d.d.map(s)),e);return i.initializeClassElements(d.F,f.elements),i.runClassFinishers(d.F,f.finishers)}function o(){o=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var i=t.placement;if(t.kind===n&&("static"===i||"prototype"===i)){var o="static"===i?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var n=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],n=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,i);r.push(t.element),r.push.apply(r,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:r,finishers:n};var o=this.decorateConstructor(r,t);return n.push.apply(n,o.finishers),o.finishers=n,o},addElementPlacement:function(e,t,r){var n=t[e.placement];if(!r&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var r=[],n=[],i=e.decorators,o=i.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,i[o])(a)||a);e=c.element,this.addElementPlacement(e,t),c.finisher&&n.push(c.finisher);var l=c.extras;if(l){for(var u=0;u<l.length;u++)this.addElementPlacement(l[u],t);r.push.apply(r,l)}}return{element:e,finishers:n,extras:r}},decorateConstructor:function(e,t){for(var r=[],n=t.length-1;n>=0;n--){var i=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[n])(i)||i);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?f(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=d(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:n,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:u(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=u(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var n=(0,t[r])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=d(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function a(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function l(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function u(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function d(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function p(){return p="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var n=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=h(e)););return e}(e,t);if(n){var i=Object.getOwnPropertyDescriptor(n,t);return i.get?i.get.call(arguments.length<3?e:r):i.value}},p.apply(this,arguments)}function h(e){return h=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},h(e)}const y=e=>i(null,(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){p(h(r.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if(p(h(r.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){const e=this.__unsubs.pop();e instanceof Promise?e.then((e=>e())):e()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(e){if(p(h(r.prototype),"updated",this).call(this,e),e.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps)for(const t of e.keys())if(this.hassSubscribeRequiredHostProps.includes(t))return void this.__checkSubscribed()}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var e;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(e=this.hassSubscribeRequiredHostProps)&&void 0!==e&&e.some((e=>void 0===this[e]))||(this.__unsubs=this.hassSubscribe())}}]}}),e)},9928:function(e,t,r){r.r(t);var n=r(37500),i=r(36924),o=r(8636),s=(r(51187),r(18457)),a=(r(22098),r(52039),r(55424)),c=r(38014),l=r(73826);function u(){u=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var i=t.placement;if(t.kind===n&&("static"===i||"prototype"===i)){var o="static"===i?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var n=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],n=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!p(e))return r.push(e);var t=this.decorateElement(e,i);r.push(t.element),r.push.apply(r,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:r,finishers:n};var o=this.decorateConstructor(r,t);return n.push.apply(n,o.finishers),o.finishers=n,o},addElementPlacement:function(e,t,r){var n=t[e.placement];if(!r&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var r=[],n=[],i=e.decorators,o=i.length-1;o>=0;o--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var a=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,i[o])(a)||a);e=c.element,this.addElementPlacement(e,t),c.finisher&&n.push(c.finisher);var l=c.extras;if(l){for(var u=0;u<l.length;u++)this.addElementPlacement(l[u],t);r.push.apply(r,l)}}return{element:e,finishers:n,extras:r}},decorateConstructor:function(e,t){for(var r=[],n=t.length-1;n>=0;n--){var i=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[n])(i)||i);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var s=0;s<e.length-1;s++)for(var a=s+1;a<e.length;a++)if(e[s].key===e[a].key&&e[s].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return g(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?g(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=m(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:n,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:y(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=y(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var n=(0,t[r])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function d(e){var t,r=m(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function f(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function p(e){return e.decorators&&e.decorators.length}function h(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function y(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function m(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function g(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}const v=238.76104;!function(e,t,r,n){var i=u();if(n)for(var o=0;o<n.length;o++)i=n[o](i);var s=t((function(e){i.initializeInstanceElements(e,a.elements)}),r),a=i.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},n=0;n<e.length;n++){var i,o=e[n];if("method"===o.kind&&(i=t.find(r)))if(h(o.descriptor)||h(i.descriptor)){if(p(o)||p(i))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");i.descriptor=o.descriptor}else{if(p(o)){if(p(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");i.decorators=o.decorators}f(o,i)}else t.push(o)}return t}(s.d.map(d)),e);i.initializeClassElements(s.F,a.elements),i.runClassFinishers(s.F,a.finishers)}([(0,i.Mo)("hui-energy-distribution-card")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return["_config"]}},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"hassSubscribe",value:function(){var e;return[(0,a.UB)(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((e=>{this._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"render",value:function(){var e,t;if(!this._config)return n.dy``;if(!this._data)return n.dy`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;const r=this._data.prefs,i=(0,a.Jj)(r),l=void 0!==i.solar,u=void 0!==i.battery,d=void 0!==i.gas,f=i.grid[0].flow_to.length>0,p=null!==(e=(0,c.q6)(this._data.stats,i.grid[0].flow_from.map((e=>e.stat_energy_from))))&&void 0!==e?e:0;let h=null;var y;d&&(h=null!==(y=(0,c.q6)(this._data.stats,i.gas.map((e=>e.stat_energy_from))))&&void 0!==y?y:0);let m=null;l&&(m=(0,c.q6)(this._data.stats,i.solar.map((e=>e.stat_energy_from)))||0);let g=null,b=null;u&&(g=(0,c.q6)(this._data.stats,i.battery.map((e=>e.stat_energy_to)))||0,b=(0,c.q6)(this._data.stats,i.battery.map((e=>e.stat_energy_from)))||0);let _=null;f&&(_=(0,c.q6)(this._data.stats,i.grid[0].flow_to.map((e=>e.stat_energy_to)))||0);let k=null;l&&(k=(m||0)-(_||0)-(g||0));let w=null,E=null;null!==k&&k<0&&(u&&(w=-1*k,w>p&&(E=Math.min(0,w-p),w=p)),k=0);let C=null;l&&u?(E||(E=Math.max(0,(_||0)-(m||0)-(g||0)-(w||0))),C=g-(w||0)):!l&&u&&(E=_);let x=null;u&&(x=(b||0)-(E||0));const S=Math.max(0,p-(w||0)),P=Math.max(0,S+(k||0)+(x||0));let $,M,D,L,Z;l&&($=v*(k/P)),x&&(M=v*(x/P));let T="https://app.electricitymap.org";if(this._data.co2SignalEntity&&this._data.fossilEnergyConsumption){const e=Object.values(this._data.fossilEnergyConsumption).reduce(((e,t)=>e+t),0),t=this.hass.states[this._data.co2SignalEntity];if(null!=t&&t.attributes.country_code&&(T+=`/zone/${t.attributes.country_code}`),null!==e){let t;D=p-e,t=S!==p?e*(S/p):e,Z=v*(t/P),L=v-($||0)-(M||0)-Z}}const H=S+(k||0)+(_?_-(E||0):0)+(C||0)+(x||0)+(w||0)+(E||0);return n.dy`
      <ha-card .header=${this._config.title}>
        <div class="card-content">
          ${void 0!==D||l||d?n.dy`<div class="row">
                ${void 0===D?n.dy`<div class="spacer"></div>`:n.dy`<div class="circle-container low-carbon">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.non_fossil")}</span
                      >
                      <a
                        class="circle"
                        href=${T}
                        target="_blank"
                        rel="noopener no referrer"
                      >
                        <ha-svg-icon .path=${"M17,8C8,10 5.9,16.17 3.82,21.34L5.71,22L6.66,19.7C7.14,19.87 7.64,20 8,20C19,20 22,3 22,3C21,5 14,5.25 9,6.25C4,7.25 2,11.5 2,13.5C2,15.5 3.75,17.25 3.75,17.25C7,8 17,8 17,8Z"}></ha-svg-icon>
                        ${D?(0,s.uf)(D,this.hass.locale,{maximumFractionDigits:1}):"—"}
                        kWh
                      </a>
                      <svg width="80" height="30">
                        <line x1="40" y1="0" x2="40" y2="30"></line>
                      </svg>
                    </div>`}
                ${l?n.dy`<div class="circle-container solar">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.solar")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${"M11.45,2V5.55L15,3.77L11.45,2M10.45,8L8,10.46L11.75,11.71L10.45,8M2,11.45L3.77,15L5.55,11.45H2M10,2H2V10C2.57,10.17 3.17,10.25 3.77,10.25C7.35,10.26 10.26,7.35 10.27,3.75C10.26,3.16 10.17,2.57 10,2M17,22V16H14L19,7V13H22L17,22Z"}></ha-svg-icon>
                        ${(0,s.uf)(m||0,this.hass.locale,{maximumFractionDigits:1})}
                        kWh
                      </div>
                    </div>`:d?n.dy`<div class="spacer"></div>`:""}
                ${d?n.dy`<div class="circle-container gas">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.gas")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${"M17.66 11.2C17.43 10.9 17.15 10.64 16.89 10.38C16.22 9.78 15.46 9.35 14.82 8.72C13.33 7.26 13 4.85 13.95 3C13 3.23 12.17 3.75 11.46 4.32C8.87 6.4 7.85 10.07 9.07 13.22C9.11 13.32 9.15 13.42 9.15 13.55C9.15 13.77 9 13.97 8.8 14.05C8.57 14.15 8.33 14.09 8.14 13.93C8.08 13.88 8.04 13.83 8 13.76C6.87 12.33 6.69 10.28 7.45 8.64C5.78 10 4.87 12.3 5 14.47C5.06 14.97 5.12 15.47 5.29 15.97C5.43 16.57 5.7 17.17 6 17.7C7.08 19.43 8.95 20.67 10.96 20.92C13.1 21.19 15.39 20.8 17.03 19.32C18.86 17.66 19.5 15 18.56 12.72L18.43 12.46C18.22 12 17.66 11.2 17.66 11.2M14.5 17.5C14.22 17.74 13.76 18 13.4 18.1C12.28 18.5 11.16 17.94 10.5 17.28C11.69 17 12.4 16.12 12.61 15.23C12.78 14.43 12.46 13.77 12.33 13C12.21 12.26 12.23 11.63 12.5 10.94C12.69 11.32 12.89 11.7 13.13 12C13.9 13 15.11 13.44 15.37 14.8C15.41 14.94 15.43 15.08 15.43 15.23C15.46 16.05 15.1 16.95 14.5 17.5H14.5Z"}></ha-svg-icon>
                        ${(0,s.uf)(h||0,this.hass.locale,{maximumFractionDigits:1})}
                        ${(0,a.vE)(r,this._data.statsMetadata)||"m³"}
                      </div>
                      <svg width="80" height="30">
                        <path d="M40 0 v30" id="gas" />
                        ${h?n.YP`<circle
                    r="1"
                    class="gas"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="2s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#gas" />
                    </animateMotion>
                  </circle>`:""}
                      </svg>
                    </div>`:n.dy`<div class="spacer"></div>`}
              </div>`:""}
          <div class="row">
            <div class="circle-container grid">
              <div class="circle">
                <ha-svg-icon .path=${"M8.28,5.45L6.5,4.55L7.76,2H16.23L17.5,4.55L15.72,5.44L15,4H9L8.28,5.45M18.62,8H14.09L13.3,5H10.7L9.91,8H5.38L4.1,10.55L5.89,11.44L6.62,10H17.38L18.1,11.45L19.89,10.56L18.62,8M17.77,22H15.7L15.46,21.1L12,15.9L8.53,21.1L8.3,22H6.23L9.12,11H11.19L10.83,12.35L12,14.1L13.16,12.35L12.81,11H14.88L17.77,22M11.4,15L10.5,13.65L9.32,18.13L11.4,15M14.68,18.12L13.5,13.64L12.6,15L14.68,18.12Z"}></ha-svg-icon>
                ${null!==_?n.dy`<span class="return">
                      <ha-svg-icon
                        class="small"
                        .path=${"M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"}
                      ></ha-svg-icon
                      >${(0,s.uf)(_,this.hass.locale,{maximumFractionDigits:1})}
                      kWh
                    </span>`:""}
                <span class="consumption">
                  ${f?n.dy`<ha-svg-icon
                        class="small"
                        .path=${"M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"}
                      ></ha-svg-icon>`:""}${(0,s.uf)(p,this.hass.locale,{maximumFractionDigits:1})}
                  kWh
                </span>
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.grid")}</span
              >
            </div>
            <div class="circle-container home">
              <div
                class="circle ${(0,o.$)({border:void 0===$&&void 0===L})}"
              >
                <ha-svg-icon .path=${"M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z"}></ha-svg-icon>
                ${(0,s.uf)(P,this.hass.locale,{maximumFractionDigits:1})}
                kWh
                ${void 0!==$||void 0!==L?n.dy`<svg>
                      ${void 0!==$?n.YP`<circle
                            class="solar"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${$} ${v-$}"
                            shape-rendering="geometricPrecision"
                            stroke-dashoffset="-${v-$}"
                          />`:""}
                      ${M?n.YP`<circle
                            class="battery"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${M} ${v-M}"
                            stroke-dashoffset="-${v-M-($||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      ${L?n.YP`<circle
                            class="low-carbon"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${L} ${v-L}"
                            stroke-dashoffset="-${v-L-(M||0)-($||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      <circle
                        class="grid"
                        cx="40"
                        cy="40"
                        r="38"
                        stroke-dasharray="${null!==(t=Z)&&void 0!==t?t:v-$-(M||0)} ${void 0!==Z?v-Z:$+(M||0)}"
                        stroke-dashoffset="0"
                        shape-rendering="geometricPrecision"
                      />
                    </svg>`:""}
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.home")}</span
              >
            </div>
          </div>
          ${u?n.dy`<div class="row">
                <div class="spacer"></div>
                <div class="circle-container battery">
                  <div class="circle">
                    <ha-svg-icon .path=${"M16 20H8V6H16M16.67 4H15V2H9V4H7.33C6.6 4 6 4.6 6 5.33V20.67C6 21.4 6.6 22 7.33 22H16.67C17.41 22 18 21.41 18 20.67V5.33C18 4.6 17.4 4 16.67 4M15 16H9V19H15V16M15 7H9V10H15V7M15 11.5H9V14.5H15V11.5Z"}></ha-svg-icon>
                    <span class="battery-in">
                      <ha-svg-icon
                        class="small"
                        .path=${"M11,4H13V16L18.5,10.5L19.92,11.92L12,19.84L4.08,11.92L5.5,10.5L11,16V4Z"}
                      ></ha-svg-icon
                      >${(0,s.uf)(g||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                    <span class="battery-out">
                      <ha-svg-icon
                        class="small"
                        .path=${"M13,20H11V8L5.5,13.5L4.08,12.08L12,4.16L19.92,12.08L18.5,13.5L13,8V20Z"}
                      ></ha-svg-icon
                      >${(0,s.uf)(b||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                  </div>
                  <span class="label"
                    >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.battery")}</span
                  >
                </div>
                <div class="spacer"></div>
              </div>`:""}
          <div class="lines ${(0,o.$)({battery:u})}">
            <svg
              viewBox="0 0 100 100"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
            >
              ${f&&l?n.YP`<path
                    id="return"
                    class="return"
                    d="M${u?45:47},0 v15 c0,${u?"35 -10,30 -30,30":"40 -10,35 -30,35"} h-20"
                    vector-effect="non-scaling-stroke"
                  ></path> `:""}
              ${l?n.YP`<path
                    id="solar"
                    class="solar"
                    d="M${u?55:53},0 v15 c0,${u?"35 10,30 30,30":"40 10,35 30,35"} h20"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              ${u?n.YP`<path
                    id="battery-house"
                    class="battery-house"
                    d="M55,100 v-15 c0,-35 10,-30 30,-30 h20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  <path
                    id="battery-grid"
                    class=${(0,o.$)({"battery-from-grid":Boolean(w),"battery-to-grid":Boolean(E)})}
                    d="M45,100 v-15 c0,-35 -10,-30 -30,-30 h-20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  `:""}
              ${u&&l?n.YP`<path
                    id="battery-solar"
                    class="battery-solar"
                    d="M50,0 V100"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              <path
                class="grid"
                id="grid"
                d="M0,${u?50:l?56:53} H100"
                vector-effect="non-scaling-stroke"
              ></path>
              ${_&&l?n.YP`<circle
                    r="1"
                    class="return"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-(_-(E||0))/H*6}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#return" />
                    </animateMotion>
                  </circle>`:""}
              ${k?n.YP`<circle
                    r="1"
                    class="solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-k/H*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#solar" />
                    </animateMotion>
                  </circle>`:""}
              ${S?n.YP`<circle
                    r="1"
                    class="grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-S/H*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#grid" />
                    </animateMotion>
                  </circle>`:""}
              ${C?n.YP`<circle
                    r="1"
                    class="battery-solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-C/H*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-solar" />
                    </animateMotion>
                  </circle>`:""}
              ${x?n.YP`<circle
                    r="1"
                    class="battery-house"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-x/H*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-house" />
                    </animateMotion>
                  </circle>`:""}
              ${w?n.YP`<circle
                    r="1"
                    class="battery-from-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-w/H*5}s"
                      repeatCount="indefinite"
                      keyPoints="1;0" keyTimes="0;1"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
              ${E?n.YP`<circle
                    r="1"
                    class="battery-to-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-E/H*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
            </svg>
          </div>
        </div>
        ${this._config.link_dashboard?n.dy`
              <div class="card-actions">
                <a href="/energy"
                  ><mwc-button>
                    ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.go_to_energy_dashboard")}
                  </mwc-button></a
                >
              </div>
            `:""}
      </ha-card>
    `}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    :host {
      --mdc-icon-size: 24px;
    }
    ha-card {
      min-width: 210px;
    }
    .card-content {
      position: relative;
      direction: ltr;
    }
    .lines {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 146px;
      display: flex;
      justify-content: center;
      padding: 0 16px 16px;
      box-sizing: border-box;
    }
    .lines.battery {
      bottom: 100px;
      height: 156px;
    }
    .lines svg {
      width: calc(100% - 160px);
      height: 100%;
      max-width: 340px;
    }
    .row {
      display: flex;
      justify-content: space-between;
      max-width: 500px;
      margin: 0 auto;
    }
    .circle-container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .circle-container.low-carbon {
      margin-right: 4px;
    }
    .circle-container.solar {
      margin: 0 4px;
      height: 130px;
    }
    .circle-container.gas {
      margin-left: 4px;
      height: 130px;
    }
    .circle-container.battery {
      height: 110px;
      justify-content: flex-end;
    }
    .spacer {
      width: 84px;
    }
    .circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      box-sizing: border-box;
      border: 2px solid;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 12px;
      line-height: 12px;
      position: relative;
      text-decoration: none;
      color: var(--primary-text-color);
    }
    ha-svg-icon {
      padding-bottom: 2px;
    }
    ha-svg-icon.small {
      --mdc-icon-size: 12px;
    }
    .label {
      color: var(--secondary-text-color);
      font-size: 12px;
    }
    line,
    path {
      stroke: var(--primary-text-color);
      stroke-width: 1;
      fill: none;
    }
    .circle svg {
      position: absolute;
      fill: none;
      stroke-width: 4px;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
    }
    .gas path,
    .gas circle {
      stroke: var(--energy-gas-color);
    }
    circle.gas {
      stroke-width: 4;
      fill: var(--energy-gas-color);
    }
    .gas .circle {
      border-color: var(--energy-gas-color);
    }
    .low-carbon line {
      stroke: var(--energy-non-fossil-color);
    }
    .low-carbon .circle {
      border-color: var(--energy-non-fossil-color);
    }
    .low-carbon ha-svg-icon {
      color: var(--energy-non-fossil-color);
    }
    circle.low-carbon {
      stroke: var(--energy-non-fossil-color);
      fill: var(--energy-non-fossil-color);
    }
    .solar .circle {
      border-color: var(--energy-solar-color);
    }
    circle.solar,
    path.solar {
      stroke: var(--energy-solar-color);
    }
    circle.solar {
      stroke-width: 4;
      fill: var(--energy-solar-color);
    }
    .battery .circle {
      border-color: var(--energy-battery-in-color);
    }
    circle.battery,
    path.battery {
      stroke: var(--energy-battery-out-color);
    }
    path.battery-house,
    circle.battery-house {
      stroke: var(--energy-battery-out-color);
    }
    circle.battery-house {
      stroke-width: 4;
      fill: var(--energy-battery-out-color);
    }
    path.battery-solar,
    circle.battery-solar {
      stroke: var(--energy-battery-in-color);
    }
    circle.battery-solar {
      stroke-width: 4;
      fill: var(--energy-battery-in-color);
    }
    .battery-in {
      color: var(--energy-battery-in-color);
    }
    .battery-out {
      color: var(--energy-battery-out-color);
    }
    path.battery-from-grid {
      stroke: var(--energy-grid-consumption-color);
    }
    path.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    path.return,
    circle.return,
    circle.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    circle.return,
    circle.battery-to-grid {
      stroke-width: 4;
      fill: var(--energy-grid-return-color);
    }
    .return {
      color: var(--energy-grid-return-color);
    }
    .grid .circle {
      border-color: var(--energy-grid-consumption-color);
    }
    .consumption {
      color: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid,
    path.grid {
      stroke: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid {
      stroke-width: 4;
      fill: var(--energy-grid-consumption-color);
    }
    .home .circle {
      border-width: 0;
      border-color: var(--primary-color);
    }
    .home .circle.border {
      border-width: 2px;
    }
    .circle svg circle {
      animation: rotate-in 0.6s ease-in;
      transition: stroke-dashoffset 0.4s, stroke-dasharray 0.4s;
      fill: none;
    }
    @keyframes rotate-in {
      from {
        stroke-dashoffset: 238.76104;
        stroke-dasharray: 238.76104;
      }
    }
    .card-actions a {
      text-decoration: none;
    }
  `}}]}}),(0,l.f)(n.oi))},76775:function(e,t,r){function n(e){return n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},n(e)}r.d(t,{Z:function(){return n}})}}]);
//# sourceMappingURL=415c7e72.js.map