"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[83407],{14166:(e,t,r)=>{r.d(t,{W:()=>n});var i=function(){return i=Object.assign||function(e){for(var t,r=1,i=arguments.length;r<i;r++)for(var n in t=arguments[r])Object.prototype.hasOwnProperty.call(t,n)&&(e[n]=t[n]);return e},i.apply(this,arguments)};function n(e,t,r){void 0===t&&(t=Date.now()),void 0===r&&(r={});var n=i(i({},o),r||{}),a=(+e-+t)/1e3;if(Math.abs(a)<n.second)return{value:Math.round(a),unit:"second"};var s=a/60;if(Math.abs(s)<n.minute)return{value:Math.round(s),unit:"minute"};var l=a/3600;if(Math.abs(l)<n.hour)return{value:Math.round(l),unit:"hour"};var c=a/86400;if(Math.abs(c)<n.day)return{value:Math.round(c),unit:"day"};var d=new Date(e),h=new Date(t),u=d.getFullYear()-h.getFullYear();if(Math.round(Math.abs(u))>0)return{value:Math.round(u),unit:"year"};var p=12*u+d.getMonth()-h.getMonth();if(Math.round(Math.abs(p))>0)return{value:Math.round(p),unit:"month"};var f=a/604800;return{value:Math.round(f),unit:"week"}}var o={second:45,minute:45,hour:22,day:5}},43986:(e,t,r)=>{r.d(t,{Z:()=>n,L:()=>o});var i=r(91168);const n={s:1,min:60,h:3600,d:86400},o=(e,t)=>(0,i.Z)(parseFloat(e)*n[t])||"0"},49684:(e,t,r)=>{r.a(e,(async e=>{r.d(t,{mr:()=>a,Vu:()=>l,xO:()=>d});var i=r(14516),n=r(65810),o=r(54121);o.Xp&&await o.Xp;const a=(e,t)=>s(t).format(e),s=(0,i.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,n.y)(e)?e.language:"en-u-hc-h23",{hour:"numeric",minute:"2-digit",hour12:(0,n.y)(e)}))),l=(e,t)=>c(t).format(e),c=(0,i.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,n.y)(e)?e.language:"en-u-hc-h23",{hour:(0,n.y)(e)?"numeric":"2-digit",minute:"2-digit",second:"2-digit",hour12:(0,n.y)(e)}))),d=(e,t)=>h(t).format(e),h=(0,i.Z)((e=>new Intl.DateTimeFormat("en"!==e.language||(0,n.y)(e)?e.language:"en-u-hc-h23",{weekday:"long",hour:(0,n.y)(e)?"numeric":"2-digit",minute:"2-digit",hour12:(0,n.y)(e)})));e()}),1)},5435:(e,t,r)=>{r.a(e,(async e=>{r.d(t,{G:()=>s});var i=r(14166),n=r(14516),o=r(54121);o.Xp&&await o.Xp;const a=(0,n.Z)((e=>new Intl.RelativeTimeFormat(e.language,{numeric:"auto"}))),s=(e,t,r,n=!0)=>{const o=(0,i.W)(e,r);return n?a(t).format(o.value,o.unit):Intl.NumberFormat(t.language,{style:"unit",unit:o.unit,unitDisplay:"long"}).format(Math.abs(o.value))};e()}),1)},91168:(e,t,r)=>{r.d(t,{Z:()=>n});const i=e=>e<10?`0${e}`:e;function n(e){const t=Math.floor(e/3600),r=Math.floor(e%3600/60),n=Math.floor(e%3600%60);return t>0?`${t}:${i(r)}:${i(n)}`:r>0?`${r}:${i(n)}`:n>0?""+n:null}},29171:(e,t,r)=>{r.a(e,(async e=>{r.d(t,{D:()=>p,c:()=>f});var i=r(56007),n=r(24833),o=r(12198),a=r(44583),s=r(49684),l=r(18457),c=r(40095),d=r(43986),h=r(58831),u=e([a,s,o]);[a,s,o]=u.then?await u:u;const p=(e,t,r,i)=>f(e,r,t.entity_id,t.attributes,void 0!==i?i:t.state),f=(e,t,r,u,p)=>{if(p===i.lz||p===i.nZ)return e(`state.default.${p}`);if((0,l.sJ)(u)){if("duration"===u.device_class&&u.unit_of_measurement&&d.Z[u.unit_of_measurement])try{return(0,d.L)(p,u.unit_of_measurement)}catch(e){}if("monetary"===u.device_class)try{return(0,l.uf)(p,t,{style:"currency",currency:u.unit_of_measurement,minimumFractionDigits:2})}catch(e){}return`${(0,l.uf)(p,t)}${u.unit_of_measurement?" "+u.unit_of_measurement:""}`}const f=(0,h.M)(r);if("input_datetime"===f){if(void 0===p){let e;return u.has_date&&u.has_time?(e=new Date(u.year,u.month-1,u.day,u.hour,u.minute),(0,a.o0)(e,t)):u.has_date?(e=new Date(u.year,u.month-1,u.day),(0,o.p6)(e,t)):u.has_time?(e=new Date,e.setHours(u.hour,u.minute),(0,s.mr)(e,t)):p}try{const e=p.split(" ");if(2===e.length)return(0,a.o0)(new Date(e.join("T")),t);if(1===e.length){if(p.includes("-"))return(0,o.p6)(new Date(`${p}T00:00`),t);if(p.includes(":")){const e=new Date;return(0,s.mr)(new Date(`${e.toISOString().split("T")[0]}T${p}`),t)}}return p}catch(e){return p}}if("humidifier"===f&&"on"===p&&u.humidity)return`${u.humidity} %`;if("counter"===f||"number"===f||"input_number"===f)return(0,l.uf)(p,t);if("button"===f||"input_button"===f||"scene"===f||"sensor"===f&&"timestamp"===u.device_class)try{return(0,a.o0)(new Date(p),t)}catch(e){return p}var m;return"update"===f?"on"===p?(0,n.X4)(u)?(0,c.f)(u,n.k6)?e("ui.card.update.installing_with_progress",{progress:u.in_progress}):e("ui.card.update.installing"):u.latest_version:u.skipped_version===u.latest_version?null!==(m=u.latest_version)&&void 0!==m?m:e("state.default.unavailable"):e("ui.card.update.up_to_date"):u.device_class&&e(`component.${f}.state.${u.device_class}.${p}`)||e(`component.${f}.state._.${p}`)||p}}))},43793:(e,t,r)=>{r.d(t,{x:()=>i});const i=(e,t)=>e.substring(0,t.length)===t},42952:(e,t,r)=>{r.a(e,(async e=>{var t=r(37500),i=r(33310),n=r(5435),o=r(21780),a=e([n]);function s(){s=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!d(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?f(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=p(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:u(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=u(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function l(e){var t,r=p(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function c(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function d(e){return e.decorators&&e.decorators.length}function h(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function u(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function p(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function m(e,t,r){return m="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=y(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(r):n.value}},m(e,t,r||e)}function y(e){return y=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},y(e)}n=(a.then?await a:a)[0];!function(e,t,r,i){var n=s();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(h(o.descriptor)||h(n.descriptor)){if(d(o)||d(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(d(o)){if(d(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}c(o,n)}else t.push(o)}return t}(a.d.map(l)),e);n.initializeClassElements(a.F,u.elements),n.runClassFinishers(a.F,u.finishers)}([(0,i.Mo)("ha-relative-time")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"datetime",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"capitalize",value:()=>!1},{kind:"field",key:"_interval",value:void 0},{kind:"method",key:"disconnectedCallback",value:function(){m(y(r.prototype),"disconnectedCallback",this).call(this),this._clearInterval()}},{kind:"method",key:"connectedCallback",value:function(){m(y(r.prototype),"connectedCallback",this).call(this),this.datetime&&this._startInterval()}},{kind:"method",key:"createRenderRoot",value:function(){return this}},{kind:"method",key:"firstUpdated",value:function(e){m(y(r.prototype),"firstUpdated",this).call(this,e),this._updateRelative()}},{kind:"method",key:"update",value:function(e){m(y(r.prototype),"update",this).call(this,e),this._updateRelative()}},{kind:"method",key:"_clearInterval",value:function(){this._interval&&(window.clearInterval(this._interval),this._interval=void 0)}},{kind:"method",key:"_startInterval",value:function(){this._clearInterval(),this._interval=window.setInterval((()=>this._updateRelative()),6e4)}},{kind:"method",key:"_updateRelative",value:function(){if(this.datetime){const e=(0,n.G)(new Date(this.datetime),this.hass.locale);this.innerHTML=this.capitalize?(0,o.f)(e):e}else this.innerHTML=this.hass.localize("ui.components.relative_time.never")}}]}}),t.fl)}))},148:(e,t,r)=>{var i=r(37500),n=r(33310),o=r(11654);r(52039);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(h.d.map(s)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,n.Mo)("ha-timeline")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"label",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"raised",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"notEnabled",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"lastItem",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"icon",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"moreItems",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_showMore",value:()=>!1},{kind:"method",key:"render",value:function(){return i.dy`
      <div class="timeline-start">
        ${this.label?"":i.dy`
              <ha-svg-icon .path=${this.icon||"M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"}></ha-svg-icon>
            `}
        ${this.lastItem?"":i.dy`<div class="line"></div>`}
      </div>
      <div class="content">
        <slot></slot>
        ${this.moreItems?i.dy`
              <div>
                ${this._showMore||1===this.moreItems.length?this.moreItems:i.dy`
                      <button class="link" @click=${this._handleShowMore}>
                        Show ${this.moreItems.length} more items
                      </button>
                    `}
              </div>
            `:""}
      </div>
    `}},{kind:"method",key:"_handleShowMore",value:function(){this._showMore=!0}},{kind:"get",static:!0,key:"styles",value:function(){return[i.iv`
        :host {
          display: flex;
          flex-direction: row;
        }
        :host(:not([lastItem])) {
          min-height: 50px;
        }
        :host([label]) {
          margin-top: -8px;
          font-style: italic;
          color: var(--timeline-label-color, var(--secondary-text-color));
        }
        .timeline-start {
          display: flex;
          flex-direction: column;
          align-items: center;
          margin-right: 8px;
          width: 24px;
        }
        :host([notEnabled]) ha-svg-icon {
          opacity: 0.5;
        }
        ha-svg-icon {
          color: var(
            --timeline-ball-color,
            var(--timeline-color, var(--secondary-text-color))
          );
          border-radius: 50%;
        }
        :host([raised]) ha-svg-icon {
          transform: scale(1.3);
        }
        .line {
          flex: 1;
          width: 2px;
          background-color: var(
            --timeline-line-color,
            var(--timeline-color, var(--secondary-text-color))
          );
          margin: 4px 0;
        }
        .content {
          margin-top: 2px;
        }
        :host(:not([lastItem])) .content {
          padding-bottom: 16px;
        }
        :host([label]) .content {
          margin-top: 0;
          padding-top: 6px;
        }
      `,o.k1]}}]}}),i.oi)},71955:(e,t,r)=>{var i=r(77426),n=r(37500),o=r(33310);r(53822),r(10983);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(h.d.map(s)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,o.Mo)("ha-trace-blueprint-config")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"method",key:"render",value:function(){return n.dy`
      <ha-code-editor
        .value=${(0,i.$w)(this.trace.blueprint_inputs||"").trimRight()}
        readOnly
        dir="ltr"
      ></ha-code-editor>
    `}}]}}),n.oi)},13126:(e,t,r)=>{var i=r(77426),n=r(37500),o=r(33310);r(53822),r(10983);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(h.d.map(s)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,o.Mo)("ha-trace-config")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"method",key:"render",value:function(){return n.dy`
      <ha-code-editor
        .value=${(0,i.$w)(this.trace.config).trimRight()}
        readOnly
        dir="ltr"
      ></ha-code-editor>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return[n.iv``]}}]}}),n.oi)},89497:(e,t,r)=>{r.a(e,(async e=>{var t=r(37500),i=r(33310),n=(r(5588),r(44198)),o=e([n]);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}n=(o.then?await o:o)[0];!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(h.d.map(s)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,i.Mo)("ha-trace-logbook")],(function(e,r){return{F:class extends r{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"logbookEntries",value:void 0},{kind:"method",key:"render",value:function(){return this.logbookEntries.length?t.dy`
          <ha-logbook-renderer
            relative-time
            .hass=${this.hass}
            .entries=${this.logbookEntries}
            .narrow=${this.narrow}
          ></ha-logbook-renderer>
          <hat-logbook-note .domain=${this.trace.domain}></hat-logbook-note>
        `:t.dy`<div class="padded-box">
          No Logbook entries found for this step.
        </div>`}},{kind:"get",static:!0,key:"styles",value:function(){return[t.iv`
        .padded-box {
          padding: 16px;
        }
      `]}}]}}),t.oi)}))},78940:(e,t,r)=>{r.a(e,(async e=>{var t=r(77426),i=r(37500),n=r(33310),o=r(8636),a=r(44583),s=(r(53822),r(10983),r(5588),r(97389)),l=r(44198),c=r(19476),d=e([a,l]);function h(){h=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!f(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return g(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?g(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=v(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:y(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=y(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function u(e){var t,r=v(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function f(e){return e.decorators&&e.decorators.length}function m(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function y(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function v(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function g(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}[a,l]=d.then?await d:d;!function(e,t,r,i){var n=h();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(m(o.descriptor)||m(n.descriptor)){if(f(o)||f(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(f(o)){if(f(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}p(o,n)}else t.push(o)}return t}(a.d.map(u)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("ha-trace-path-details")],(function(e,r){return{F:class extends r{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"logbookEntries",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selected",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"renderedNodes",value:()=>({})},{kind:"field",decorators:[(0,n.Cb)()],key:"trackedNodes",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_view",value:()=>"config"},{kind:"method",key:"render",value:function(){return i.dy`
      <div class="padded-box trace-info">
        ${this._renderSelectedTraceInfo()}
      </div>

      <div class="tabs top">
        ${[["config","Step Config"],["changed_variables","Changed Variables"],["logbook","Related logbook entries"]].map((([e,t])=>i.dy`
            <button
              .view=${e}
              class=${(0,o.$)({active:this._view===e})}
              @click=${this._showTab}
            >
              ${t}
            </button>
          `))}
      </div>
      ${"config"===this._view?this._renderSelectedConfig():"changed_variables"===this._view?this._renderChangedVars():this._renderLogbook()}
    `}},{kind:"method",key:"_renderSelectedTraceInfo",value:function(){var e;const r=this.trace.trace;if(null===(e=this.selected)||void 0===e||!e.path)return"Select a node on the left for more information.";const n=this.selected.path.split("/");if("default"===n[n.length-1]){var o,s;const e=r[n.slice(0,n.length-1).join("/")];if(e&&"default"===(null===(o=e[0])||void 0===o||null===(s=o.result)||void 0===s?void 0:s.choice))return"The default action was executed because no options matched."}if(!(this.selected.path in r))return"This node was not executed and so no further trace information is available.";const l=[];let c=!1;for(const e of Object.keys(this.trace.trace)){if(c){if(e in this.renderedNodes)break}else{if(e!==this.selected.path)continue;c=!0}const n=r[e];l.push(n.map(((r,o)=>{const{path:s,timestamp:l,result:c,error:d,changed_variables:h,...u}=r;return!1===(null==c?void 0:c.enabled)?i.dy`This node was disabled and skipped during execution so
            no further trace information is available.`:i.dy`
            ${e===this.selected.path?"":i.dy`<h2>${e.substr(this.selected.path.length+1)}</h2>`}
            ${1===n.length?"":i.dy`<h3>Iteration ${o+1}</h3>`}
            Executed:
            ${(0,a.E8)(new Date(l),this.hass.locale)}<br />
            ${c?i.dy`Result:
                  <pre>${(0,t.$w)(c)}</pre>`:d?i.dy`<div class="error">Error: ${d}</div>`:""}
            ${0===Object.keys(u).length?"":i.dy`<pre>${(0,t.$w)(u)}</pre>`}
          `})))}return l}},{kind:"method",key:"_renderSelectedConfig",value:function(){var e;if(null===(e=this.selected)||void 0===e||!e.path)return"";const r=(0,s.nV)(this.trace.config,this.selected.path);return r?i.dy`<ha-code-editor
          .value=${(0,t.$w)(r).trimRight()}
          readOnly
          dir="ltr"
        ></ha-code-editor>`:"Unable to find config"}},{kind:"method",key:"_renderChangedVars",value:function(){const e=this.trace.trace[this.selected.path];return i.dy`
      <div class="padded-box">
        ${e.map(((e,r)=>i.dy`
            ${r>0?i.dy`<p>Iteration ${r+1}</p>`:""}
            ${0===Object.keys(e.changed_variables||{}).length?"No variables changed":i.dy`<pre>${(0,t.$w)(e.changed_variables).trimRight()}</pre>`}
          `))}
      </div>
    `}},{kind:"method",key:"_renderLogbook",value:function(){const e=this.trace.trace,t=e[this.selected.path],r=Object.keys(this.trackedNodes),n=r.indexOf(this.selected.path);if(-1===n)return i.dy`<div class="padded-box">Node not tracked.</div>`;let o;if(n===r.length-1){const e=new Date(t[0].timestamp),r=this.logbookEntries.findIndex((t=>new Date(1e3*t.when)>=e));o=-1===r?[]:this.logbookEntries.slice(r)}else{const i=e[r[n+1]],a=new Date(t[0].timestamp),s=new Date(i[0].timestamp);o=[];for(const e of this.logbookEntries||[]){const t=new Date(1e3*e.when);if(t>=a){if(!(t<s))break;o.push(e)}}}return o.length?i.dy`
          <ha-logbook-renderer
            relative-time
            .hass=${this.hass}
            .entries=${o}
            .narrow=${this.narrow}
          ></ha-logbook-renderer>
          <hat-logbook-note .domain=${this.trace.domain}></hat-logbook-note>
        `:i.dy`<div class="padded-box">
          No Logbook entries found for this step.
        </div>`}},{kind:"method",key:"_showTab",value:function(e){this._view=e.target.view}},{kind:"get",static:!0,key:"styles",value:function(){return[c.b,i.iv`
        .padded-box {
          margin: 16px;
        }

        :host(:not([narrow])) .trace-info {
          min-height: 250px;
        }

        pre {
          margin: 0;
        }

        .error {
          color: var(--error-color);
        }
      `]}}]}}),i.oi)}))},7719:(e,t,r)=>{r.a(e,(async e=>{var t=r(37500),i=r(33310),n=(r(5588),r(11777)),o=e([n]);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:h(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=h(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function h(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}n=(o.then?await o:o)[0];!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(h.d.map(s)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,i.Mo)("ha-trace-timeline")],(function(e,r){return{F:class extends r{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"logbookEntries",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"selected",value:void 0},{kind:"method",key:"render",value:function(){return t.dy`
      <hat-trace-timeline
        .hass=${this.hass}
        .trace=${this.trace}
        .logbookEntries=${this.logbookEntries}
        .selectedPath=${this.selected.path}
        allowPick
      >
      </hat-trace-timeline>
      <hat-logbook-note .domain=${this.trace.domain}></hat-logbook-note>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return[t.iv`
        :host {
          display: block;
          padding: 16px;
        }
      `]}}]}}),t.oi)}))},5588:(e,t,r)=>{var i=r(37500),n=r(33310);function o(){o=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!l(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return u(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?u(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=h(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function a(e){var t,r=h(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function s(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function l(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function h(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function u(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=o();if(i)for(var d=0;d<i.length;d++)n=i[d](n);var h=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(c(o.descriptor)||c(n.descriptor)){if(l(o)||l(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(l(o)){if(l(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}s(o,n)}else t.push(o)}return t}(h.d.map(a)),e);n.initializeClassElements(h.F,u.elements),n.runClassFinishers(h.F,u.finishers)}([(0,n.Mo)("hat-logbook-note")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)()],key:"domain",value:()=>"automation"},{kind:"method",key:"render",value:function(){return i.dy`
      Not all shown logbook entries might be related to this ${this.domain}.
    `}},{kind:"field",static:!0,key:"styles",value:()=>i.iv`
    :host {
      display: block;
      text-align: center;
      font-style: italic;
      padding: 16px;
      margin-top: 8px;
    }
  `}]}}),i.oi)},54933:(e,t,r)=>{var i=r(37500),n=r(33310),o=r(47181),a=r(42141),s=(r(10983),r(8636));const l=10,c=30;function d(){d=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!p(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return v(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?v(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=y(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:m(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=m(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function h(e){var t,r=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function u(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function p(e){return e.decorators&&e.decorators.length}function f(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function m(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function v(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=d();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(f(o.descriptor)||f(n.descriptor)){if(p(o)||p(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(p(o)){if(p(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}u(o,n)}else t.push(o)}return t}(a.d.map(h)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("hat-graph-branch")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"disabled",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"selected",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"start",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"short",value:()=>!1},{kind:"field",decorators:[(0,n.SB)()],key:"_branches",value:()=>[]},{kind:"field",key:"_totalWidth",value:()=>0},{kind:"field",key:"_maxHeight",value:()=>0},{kind:"method",key:"_updateBranches",value:function(e){let t=0;const r=[],i=[];e.target.assignedElements().forEach((e=>{const n=e.clientWidth,o=e.clientHeight;i.push({x:n/2+t,height:o,start:e.hasAttribute("graphStart"),end:e.hasAttribute("graphEnd"),track:e.hasAttribute("track")}),t+=n,r.push(o)})),this._totalWidth=t,this._maxHeight=Math.max(...r),this._branches=i.sort(((e,t)=>e.track&&!t.track?1:e.track&&t.track?0:-1))}},{kind:"method",key:"render",value:function(){return i.dy`
      <slot name="head"></slot>
      ${this.start?"":i.YP`
            <svg
              id="top"
              width="${this._totalWidth}"
            >
              ${this._branches.map((e=>e.start?"":i.YP`
                  <path
                    class=${(0,s.$)({track:e.track})}
                    d="
                      M ${this._totalWidth/2} 0
                      L ${e.x} ${20}
                      "/>
                `))}
            </svg>
          `}
      <div id="branches">
        <svg id="lines" width=${this._totalWidth} height=${this._maxHeight}>
          ${this._branches.map((e=>e.end?"":i.YP`
                    <path
                      class=${(0,s.$)({track:e.track})}
                      d="
                        M ${e.x} ${e.height}
                        v ${this._maxHeight-e.height}
                        "/>
                  `))}
        </svg>
        <slot @slotchange=${this._updateBranches}></slot>
      </div>

      ${this.short?"":i.YP`
            <svg
              id="bottom"
              width="${this._totalWidth}"
            >
              ${this._branches.map((e=>e.end?"":i.YP`
                  <path
                    class=${(0,s.$)({track:e.track})}
                    d="
                      M ${e.x} 0
                      V ${l}
                      L ${this._totalWidth/2} ${30}
                      "/>
                `))}
            </svg>
          `}
    `}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      :host(:focus) {
        outline: none;
      }
      #branches {
        position: relative;
        display: flex;
        flex-direction: row;
        align-items: start;
      }
      ::slotted(*) {
        z-index: 1;
      }
      ::slotted([slot="head"]) {
        margin-bottom: calc(var(--hat-graph-branch-height) / -2);
      }
      #lines {
        position: absolute;
      }
      #top {
        height: var(--hat-graph-branch-height);
      }
      #bottom {
        height: calc(var(--hat-graph-branch-height) + var(--hat-graph-spacing));
      }
      path {
        stroke: var(--stroke-clr);
        stroke-width: 2;
        fill: none;
      }
      path.track {
        stroke: var(--track-clr);
      }
      :host([disabled]) path {
        stroke: var(--disabled-clr);
      }
    `}}]}}),i.oi);function g(){g=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!w(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return x(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?x(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=$(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:_(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=_(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function b(e){var t,r=$(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function k(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function w(e){return e.decorators&&e.decorators.length}function E(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function _(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function $(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function x(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=g();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(E(o.descriptor)||E(n.descriptor)){if(w(o)||w(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(w(o)){if(w(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}k(o,n)}else t.push(o)}return t}(a.d.map(b)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("hat-graph-node")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)()],key:"iconPath",value:void 0},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"disabled",value:void 0},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"notEnabled",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"graphStart",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"nofocus"})],key:"noFocus",value:()=>!1},{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Number})],key:"badge",value:void 0},{kind:"method",key:"updated",value:function(e){e.has("noFocus")&&(this.hasAttribute("tabindex")||this.noFocus?void 0!==e.get("noFocus")&&this.noFocus&&this.removeAttribute("tabindex"):this.setAttribute("tabindex","0"))}},{kind:"method",key:"render",value:function(){const e=c+(this.graphStart?2:11);return i.dy`
      <svg
        width="${40}px"
        height="${e}px"
        viewBox="-${Math.ceil(20)} -${this.graphStart?Math.ceil(e/2):Math.ceil(25)} ${40} ${e}"
      >
        ${this.graphStart?"":i.YP`
          <path
            class="connector"
            d="
              M 0 ${-25}
              L 0 0
            "
            line-caps="round"
          />
          `}
        <g class="node">
          <circle cx="0" cy="0" r=${15} />
          }
          ${this.badge?i.YP`
        <g class="number">
          <circle
            cx="8"
            cy=${-15}
            r="8"
          ></circle>
          <text
            x="8"
            y=${-15}
            text-anchor="middle"
            alignment-baseline="middle"
          >${this.badge>9?"9+":this.badge}</text>
        </g>
      `:""}
          <g style="pointer-events: none" transform="translate(${-12} ${-12})">
            ${this.iconPath?i.YP`<path class="icon" d=${this.iconPath}/>`:""}
          </g>
        </g>
      </svg>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        display: flex;
        flex-direction: column;
        min-width: calc(var(--hat-graph-node-size) + var(--hat-graph-spacing));
        height: calc(
          var(--hat-graph-node-size) + var(--hat-graph-spacing) + 1px
        );
      }
      :host([graphStart]) {
        height: calc(var(--hat-graph-node-size) + 2px);
      }
      :host([track]) {
        --stroke-clr: var(--track-clr);
        --icon-clr: var(--default-icon-clr);
      }
      :host([active]) circle {
        --stroke-clr: var(--active-clr);
        --icon-clr: var(--default-icon-clr);
      }
      :host(:focus) {
        outline: none;
      }
      :host(:hover) circle {
        --stroke-clr: var(--hover-clr);
        --icon-clr: var(--default-icon-clr);
      }
      :host([notEnabled]) circle {
        --stroke-clr: var(--disabled-clr);
      }
      :host([notEnabled][active]) circle {
        --stroke-clr: var(--disabled-active-clr);
      }
      :host([notEnabled]:hover) circle {
        --stroke-clr: var(--disabled-hover-clr);
      }
      svg {
        width: 100%;
        height: 100%;
      }
      circle,
      path.connector {
        stroke: var(--stroke-clr);
        stroke-width: 2;
        fill: none;
      }
      circle {
        fill: var(--background-clr);
        stroke: var(--circle-clr, var(--stroke-clr));
      }
      .number circle {
        fill: var(--track-clr);
        stroke: none;
        stroke-width: 0;
      }
      .number text {
        font-size: smaller;
      }
      path.icon {
        fill: var(--icon-clr);
      }
    `}}]}}),i.oi);function P(){P=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!D(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return O(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?O(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=z(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:T(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=T(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function C(e){var t,r=z(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function A(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function D(e){return e.decorators&&e.decorators.length}function S(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function T(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function z(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function O(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=P();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(S(o.descriptor)||S(n.descriptor)){if(D(o)||D(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(D(o)){if(D(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}A(o,n)}else t.push(o)}return t}(a.d.map(C)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("hat-graph-spacer")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({reflect:!0,type:Boolean})],key:"disabled",value:void 0},{kind:"method",key:"render",value:function(){return i.dy`
      <svg viewBox="-${5} 0 10 ${41}">
        <path
          d="
              M 0 ${41}
              V 0
            "
          line-caps="round"
        />
        }
      </svg>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      svg {
        width: var(--hat-graph-spacing);
        height: calc(
          var(--hat-graph-spacing) + var(--hat-graph-node-size) + 1px
        );
      }
      :host([track]) {
        --stroke-clr: var(--track-clr);
      }
      :host-context([disabled]) {
        --stroke-clr: var(--disabled-clr);
      }
      path {
        stroke: var(--stroke-clr);
        stroke-width: 2;
        fill: none;
      }
    `}}]}}),i.oi);function j(){j=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!M(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return N(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?N(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=H(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:V(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=V(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function I(e){var t,r=H(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function L(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function M(e){return e.decorators&&e.decorators.length}function F(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function V(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function H(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function N(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function R(e,t,r){return R="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=B(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(r):n.value}},R(e,t,r||e)}function B(e){return B=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},B(e)}const Z="M 11,4L 13,4L 13,15L 11,15L 11,4 Z M 13,18L 13,20L 11,20L 11,18L 13,18 Z";!function(e,t,r,i){var n=j();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(F(o.descriptor)||F(n.descriptor)){if(M(o)||M(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(M(o)){if(M(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}L(o,n)}else t.push(o)}return t}(a.d.map(I)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("hat-script-graph")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selected",value:void 0},{kind:"field",key:"renderedNodes",value:()=>({})},{kind:"field",key:"trackedNodes",value:()=>({})},{kind:"method",key:"selectNode",value:function(e,t){return()=>{(0,o.B)(this,"graph-node-selected",{config:e,path:t})}}},{kind:"method",key:"render_trigger",value:function(e,t){const r=`trigger/${t}`,n=this.trace&&r in this.trace.trace;return this.renderedNodes[r]={config:e,path:r},n&&(this.trackedNodes[r]=this.renderedNodes[r]),i.dy`
      <hat-graph-node
        graphStart
        ?track=${n}
        @focus=${this.selectNode(e,r)}
        ?active=${this.selected===r}
        .iconPath=${"M21 13H14.4L19.1 17.7L17.7 19.1L13 14.4V21H11V14.3L6.3 19L4.9 17.6L9.4 13H3V11H9.6L4.9 6.3L6.3 4.9L11 9.6V3H13V9.4L17.6 4.8L19 6.3L14.3 11H21V13Z"}
        .notEnabled=${!1===e.enabled}
        tabindex=${n?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_condition",value:function(e,t){const r=`condition/${t}`;return this.renderedNodes[r]={config:e,path:r},this.trace&&r in this.trace.trace&&(this.trackedNodes[r]=this.renderedNodes[r]),this.render_condition_node(e,r)}},{kind:"field",key:"typeRenderers",value(){return{condition:this.render_condition_node,and:this.render_condition_node,or:this.render_condition_node,not:this.render_condition_node,delay:this.render_delay_node,event:this.render_event_node,scene:this.render_scene_node,service:this.render_service_node,wait_template:this.render_wait_node,wait_for_trigger:this.render_wait_node,repeat:this.render_repeat_node,choose:this.render_choose_node,device_id:this.render_device_node,if:this.render_if_node,stop:this.render_stop_node,parallel:this.render_parallel_node,other:this.render_other_node}}},{kind:"method",key:"render_action_node",value:function(e,t,r=!1,i=!1){const n=Object.keys(this.typeRenderers).find((t=>t in e))||"other";return this.renderedNodes[t]={config:e,path:t},this.trace&&t in this.trace.trace&&(this.trackedNodes[t]=this.renderedNodes[t]),this.typeRenderers[n].bind(this)(e,t,r,i)}},{kind:"method",key:"render_choose_node",value:function(e,t,r=!1,n=!1){var o,s;const l=this.trace.trace[t],c=l?l.map((e=>void 0===e.result||"default"===e.result.choice?"default":e.result.choice)):[],d=c.includes("default");return i.dy`
      <hat-graph-branch
        tabindex=${void 0===l?"-1":"0"}
        @focus=${this.selectNode(e,t)}
        ?track=${void 0!==l}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      >
        <hat-graph-node
          .graphStart=${r}
          .iconPath=${"M11,5H8L12,1L16,5H13V9.43C12.25,9.89 11.58,10.46 11,11.12V5M22,11L18,7V10C14.39,9.85 11.31,12.57 11,16.17C9.44,16.72 8.62,18.44 9.17,20C9.72,21.56 11.44,22.38 13,21.83C14.56,21.27 15.38,19.56 14.83,18C14.53,17.14 13.85,16.47 13,16.17C13.47,12.17 17.47,11.97 17.95,11.97V14.97L22,11M10.63,11.59C9.3,10.57 7.67,10 6,10V7L2,11L6,15V12C7.34,12.03 8.63,12.5 9.64,13.4C9.89,12.76 10.22,12.15 10.63,11.59Z"}
          ?track=${void 0!==l}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          slot="head"
          nofocus
        ></hat-graph-node>

        ${e.choose?null===(o=(0,a.r)(e.choose))||void 0===o?void 0:o.map(((r,o)=>{const s=`${t}/choose/${o}`,d=c.includes(o);return this.renderedNodes[s]={config:e,path:s},d&&(this.trackedNodes[s]=this.renderedNodes[s]),i.dy`
                <div class="graph-container" ?track=${d}>
                  <hat-graph-node
                    .iconPath=${!l||d?"M19,19H5V5H15V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V11H19M7.91,10.08L6.5,11.5L11,16L21,6L19.59,4.58L11,13.17L7.91,10.08Z":"M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,5V19H5V5H19Z"}
                    @focus=${this.selectNode(e,s)}
                    ?track=${d}
                    ?active=${this.selected===s}
                    .notEnabled=${n||!1===e.enabled}
                  ></hat-graph-node>
                  ${null!==r.sequence?(0,a.r)(r.sequence).map(((t,r)=>this.render_action_node(t,`${s}/sequence/${r}`,!1,n||!1===e.enabled))):""}
                </div>
              `})):""}
        <div ?track=${d}>
          <hat-graph-spacer ?track=${d}></hat-graph-spacer>
          ${null!==e.default?null===(s=(0,a.r)(e.default))||void 0===s?void 0:s.map(((r,i)=>this.render_action_node(r,`${t}/default/${i}`,!1,n||!1===e.enabled))):""}
        </div>
      </hat-graph-branch>
    `}},{kind:"method",key:"render_if_node",value:function(e,t,r=!1,n=!1){const o=this.trace.trace[t];let s=!1,l=!1;for(const e of o||[]){var c,d;if(s||"then"!==(null===(c=e.result)||void 0===c?void 0:c.choice)||(s=!0),(l||"else"!==(null===(d=e.result)||void 0===d?void 0:d.choice))&&e.result||(l=!0),l&&s)break}return i.dy`
      <hat-graph-branch
        tabindex=${void 0===o?"-1":"0"}
        @focus=${this.selectNode(e,t)}
        ?track=${void 0!==o}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      >
        <hat-graph-node
          .graphStart=${r}
          .iconPath=${"M14,4L16.29,6.29L13.41,9.17L14.83,10.59L17.71,7.71L20,10V4M10,4H4V10L6.29,7.71L11,12.41V20H13V11.59L7.71,6.29"}
          ?track=${void 0!==o}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          slot="head"
          nofocus
        ></hat-graph-node>
        ${e.else?i.dy`<div class="graph-container" ?track=${l}>
              <hat-graph-node
                .iconPath=${"M19.59,7L12,14.59L6.41,9H11V7H3V15H5V10.41L12,17.41L21,8.41"}
                ?track=${l}
                ?active=${this.selected===t}
                .notEnabled=${n||!1===e.enabled}
                nofocus
              ></hat-graph-node
              >${(0,a.r)(e.else).map(((r,i)=>this.render_action_node(r,`${t}/else/${i}`,!1,n||!1===e.enabled)))}
            </div>`:i.dy`<hat-graph-spacer ?track=${l}></hat-graph-spacer>`}
        <div class="graph-container" ?track=${s}>
          <hat-graph-node
            .iconPath=${"M20,5.41L18.59,4L7,15.59V9H5V19H15V17H8.41"}
            ?track=${s}
            ?active=${this.selected===t}
            .notEnabled=${n||!1===e.enabled}
            nofocus
          ></hat-graph-node>
          ${(0,a.r)(e.then).map(((r,i)=>this.render_action_node(r,`${t}/then/${i}`,!1,n||!1===e.enabled)))}
        </div>
      </hat-graph-branch>
    `}},{kind:"method",key:"render_condition_node",value:function(e,t,r=!1,n=!1){const o=this.trace.trace[t];let a=!1,s=!1,l=!1;if(o)for(const e of o)if(e.result&&(a=!0,e.result.result?s=!0:l=!0),s&&l)break;return i.dy`
      <hat-graph-branch
        @focus=${this.selectNode(e,t)}
        ?track=${a}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${void 0===o?"-1":"0"}
        short
      >
        <hat-graph-node
          .graphStart=${r}
          slot="head"
          ?track=${a}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          .iconPath=${"M4 2A2 2 0 0 0 2 4V12H4V8H6V12H8V4A2 2 0 0 0 6 2H4M4 4H6V6H4M22 15.5V14A2 2 0 0 0 20 12H16V22H20A2 2 0 0 0 22 20V18.5A1.54 1.54 0 0 0 20.5 17A1.54 1.54 0 0 0 22 15.5M20 20H18V18H20V20M20 16H18V14H20M5.79 21.61L4.21 20.39L18.21 2.39L19.79 3.61Z"}
          nofocus
        ></hat-graph-node>
        <div
          style=${"width: 40px;"}
          graphStart
          graphEnd
        ></div>
        <div ?track=${s}></div>
        <hat-graph-node
          .iconPath=${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}
          nofocus
          ?track=${l}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
        ></hat-graph-node>
      </hat-graph-branch>
    `}},{kind:"method",key:"render_delay_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${"M12,20A7,7 0 0,1 5,13A7,7 0 0,1 12,6A7,7 0 0,1 19,13A7,7 0 0,1 12,20M19.03,7.39L20.45,5.97C20,5.46 19.55,5 19.04,4.56L17.62,6C16.07,4.74 14.12,4 12,4A9,9 0 0,0 3,13A9,9 0 0,0 12,22C17,22 21,17.97 21,13C21,10.88 20.26,8.93 19.03,7.39M11,14H13V8H11M15,1H9V3H15V1Z"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_device_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${"M3 6H21V4H3C1.9 4 1 4.9 1 6V18C1 19.1 1.9 20 3 20H7V18H3V6M13 12H9V13.78C8.39 14.33 8 15.11 8 16C8 16.89 8.39 17.67 9 18.22V20H13V18.22C13.61 17.67 14 16.88 14 16S13.61 14.33 13 13.78V12M11 17.5C10.17 17.5 9.5 16.83 9.5 16S10.17 14.5 11 14.5 12.5 15.17 12.5 16 11.83 17.5 11 17.5M22 8H16C15.5 8 15 8.5 15 9V19C15 19.5 15.5 20 16 20H22C22.5 20 23 19.5 23 19V9C23 8.5 22.5 8 22 8M21 18H17V10H21V18Z"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_event_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${Z}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_repeat_node",value:function(e,t,r=!1,n=!1){var o,s;const l=this.trace.trace[t],c=null===(o=this.trace)||void 0===o||null===(s=o.trace[`${t}/repeat/sequence/0`])||void 0===s?void 0:s.length;return i.dy`
      <hat-graph-branch
        tabindex=${void 0===l?"-1":"0"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      >
        <hat-graph-node
          .graphStart=${r}
          .iconPath=${"M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z"}
          ?track=${t in this.trace.trace}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          slot="head"
          nofocus
        ></hat-graph-node>
        <hat-graph-node
          .iconPath=${"M13,20H11V8L5.5,13.5L4.08,12.08L12,4.16L19.92,12.08L18.5,13.5L13,8V20Z"}
          ?track=${c>1}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          nofocus
          .badge=${c>1?c:void 0}
        ></hat-graph-node>
        <div ?track=${l}>
          ${(0,a.r)(e.repeat.sequence).map(((r,i)=>this.render_action_node(r,`${t}/repeat/sequence/${i}`,!1,n||!1===e.enabled)))}
        </div>
      </hat-graph-branch>
    `}},{kind:"method",key:"render_scene_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${Z}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_service_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${"M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_wait_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${"M12,9A2,2 0 0,1 10,7C10,5.89 10.9,5 12,5C13.11,5 14,5.89 14,7A2,2 0 0,1 12,9M12,14A2,2 0 0,1 10,12C10,10.89 10.9,10 12,10C13.11,10 14,10.89 14,12A2,2 0 0,1 12,14M12,19A2,2 0 0,1 10,17C10,15.89 10.9,15 12,15C13.11,15 14,15.89 14,17A2,2 0 0,1 12,19M20,10H17V8.86C18.72,8.41 20,6.86 20,5H17V4A1,1 0 0,0 16,3H8A1,1 0 0,0 7,4V5H4C4,6.86 5.28,8.41 7,8.86V10H4C4,11.86 5.28,13.41 7,13.86V15H4C4,16.86 5.28,18.41 7,18.86V20A1,1 0 0,0 8,21H16A1,1 0 0,0 17,20V18.86C18.72,18.41 20,16.86 20,15H17V13.86C18.72,13.41 20,11.86 20,10Z"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
        tabindex=${this.trace&&t in this.trace.trace?"0":"-1"}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_parallel_node",value:function(e,t,r=!1,n=!1){const o=this.trace.trace[t];return i.dy`
      <hat-graph-branch
        tabindex=${void 0===o?"-1":"0"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      >
        <hat-graph-node
          .graphStart=${r}
          .iconPath=${"M16,4.5V7H5V9H16V11.5L19.5,8M16,12.5V15H5V17H16V19.5L19.5,16"}
          ?track=${t in this.trace.trace}
          ?active=${this.selected===t}
          .notEnabled=${n||!1===e.enabled}
          slot="head"
          nofocus
        ></hat-graph-node>
        ${(0,a.r)(e.parallel).map(((r,o)=>"sequence"in r?i.dy`<div ?track=${t in this.trace.trace}>
                ${(0,a.r)(r.sequence).map(((r,i)=>this.render_action_node(r,`${t}/parallel/${o}/sequence/${i}`,!1,n||!1===e.enabled)))}
              </div>`:this.render_action_node(r,`${t}/parallel/${o}/sequence/0`,!1,n||!1===e.enabled)))}
      </hat-graph-branch>
    `}},{kind:"method",key:"render_stop_node",value:function(e,t,r=!1,n=!1){var o;const a=this.trace.trace[t];return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${null!=a&&null!==(o=a[0].result)&&void 0!==o&&o.error?"M13 13H11V7H13M11 15H13V17H11M15.73 3H8.27L3 8.27V15.73L8.27 21H15.73L21 15.73V8.27L15.73 3Z":"M8.27,3L3,8.27V15.73L8.27,21H15.73L21,15.73V8.27L15.73,3M8.41,7L12,10.59L15.59,7L17,8.41L13.41,12L17,15.59L15.59,17L12,13.41L8.41,17L7,15.59L10.59,12L7,8.41"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      ></hat-graph-node>
    `}},{kind:"method",key:"render_other_node",value:function(e,t,r=!1,n=!1){return i.dy`
      <hat-graph-node
        .graphStart=${r}
        .iconPath=${"M15,4V6H18V18H15V20H20V4M4,4V20H9V18H6V6H9V4H4Z"}
        @focus=${this.selectNode(e,t)}
        ?track=${t in this.trace.trace}
        ?active=${this.selected===t}
        .notEnabled=${n||!1===e.enabled}
      ></hat-graph-node>
    `}},{kind:"method",key:"render",value:function(){const e=Object.keys(this.trackedNodes),t="trigger"in this.trace.config?(0,a.r)(this.trace.config.trigger).map(((e,t)=>this.render_trigger(e,t))):void 0;try{var r;return i.dy`
        <div class="parent graph-container">
          ${t?i.dy`<hat-graph-branch start .short=${t.length<2}>
                ${t}
              </hat-graph-branch>`:""}
          ${"condition"in this.trace.config?i.dy`${null===(r=(0,a.r)(this.trace.config.condition))||void 0===r?void 0:r.map(((e,t)=>this.render_condition(e,t)))}`:""}
          ${"action"in this.trace.config?i.dy`${(0,a.r)(this.trace.config.action).map(((e,t)=>this.render_action_node(e,`action/${t}`)))}`:""}
          ${"sequence"in this.trace.config?i.dy`${(0,a.r)(this.trace.config.sequence).map(((e,t)=>this.render_action_node(e,`sequence/${t}`,0===t)))}`:""}
        </div>
        <div class="actions">
          <ha-icon-button
            .disabled=${0===e.length||e[0]===this.selected}
            @click=${this._previousTrackedNode}
            .path=${"M7.41,15.41L12,10.83L16.59,15.41L18,14L12,8L6,14L7.41,15.41Z"}
          ></ha-icon-button>
          <ha-icon-button
            .disabled=${0===e.length||e[e.length-1]===this.selected}
            @click=${this._nextTrackedNode}
            .path=${"M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"}
          ></ha-icon-button>
        </div>
      `}catch(e){return i.dy`
        <div class="error">
          Error rendering graph. Please download trace and share with the
          developers.
        </div>
      `}}},{kind:"method",key:"willUpdate",value:function(e){R(B(r.prototype),"willUpdate",this).call(this,e),e.has("trace")&&(this.renderedNodes={},this.trackedNodes={})}},{kind:"method",key:"updated",value:function(e){if(R(B(r.prototype),"updated",this).call(this,e),e.has("trace")){if(!this.selected||!(this.selected in this.trackedNodes)){const e=this.trackedNodes[Object.keys(this.trackedNodes)[0]];e&&(0,o.B)(this,"graph-node-selected",e)}if(this.trace){const e=Object.keys(this.trace.trace),t=Object.keys(this.renderedNodes).sort(((t,r)=>e.indexOf(t)-e.indexOf(r))),r={},i={};for(const e of t)i[e]=this.renderedNodes[e],e in this.trackedNodes&&(r[e]=this.trackedNodes[e]);this.renderedNodes=i,this.trackedNodes=r}}}},{kind:"method",key:"_previousTrackedNode",value:function(){const e=Object.keys(this.trackedNodes),t=e.indexOf(this.selected)-1;t>=0&&(0,o.B)(this,"graph-node-selected",this.trackedNodes[e[t]])}},{kind:"method",key:"_nextTrackedNode",value:function(){const e=Object.keys(this.trackedNodes),t=e.indexOf(this.selected)+1;t<e.length&&(0,o.B)(this,"graph-node-selected",this.trackedNodes[e[t]])}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        display: flex;
        --stroke-clr: var(--stroke-color, var(--secondary-text-color));
        --active-clr: var(--active-color, var(--primary-color));
        --track-clr: var(--track-color, var(--accent-color));
        --hover-clr: var(--hover-color, var(--primary-color));
        --disabled-clr: var(--disabled-color, var(--disabled-text-color));
        --disabled-active-clr: rgba(var(--rgb-primary-color), 0.5);
        --disabled-hover-clr: rgba(var(--rgb-primary-color), 0.7);
        --default-trigger-color: 3, 169, 244;
        --rgb-trigger-color: var(--trigger-color, var(--default-trigger-color));
        --background-clr: var(--background-color, white);
        --default-icon-clr: var(--icon-color, black);
        --icon-clr: var(--stroke-clr);

        --hat-graph-spacing: ${l}px;
        --hat-graph-node-size: ${c}px;
        --hat-graph-branch-height: ${20}px;
      }
      .graph-container {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .actions {
        display: flex;
        flex-direction: column;
      }
      .parent {
        margin-left: 8px;
        margin-top: 16px;
      }
      .error {
        padding: 16px;
        max-width: 300px;
      }
    `}}]}}),i.oi)},11777:(e,t,r)=>{r.a(e,(async e=>{var t=r(37500),i=r(33310),n=r(51346),o=r(44583),a=r(5435),s=r(47181),l=r(70518),c=r(44547),d=r(59847),h=r(97389),u=(r(148),e([o,a]));function p(){p=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!y(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return k(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?k(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=b(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:g(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=g(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function f(e){var t,r=b(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function m(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function y(e){return e.decorators&&e.decorators.length}function v(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function g(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function b(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function w(e,t,r){return w="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=E(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(r):n.value}},w(e,t,r||e)}function E(e){return E=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},E(e)}function _(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}[o,a]=u.then?await u:u;const $="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z",x="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z",P=(e,t)=>Math.abs(t.getTime()-e.getTime())>1e3;class C{constructor(e,t,r){this.hass=e,this.entries=t,_(this,"lastReportedTime",void 0),this.lastReportedTime=new Date(r.timestamp.start)}setLastReportedTime(e){this.lastReportedTime=e}renderTime(e,r){this.entries.push(t.dy`
      <ha-timeline label>
        ${(0,a.G)(e,this.hass.locale,r,!1)} later
      </ha-timeline>
    `),this.lastReportedTime=r}maybeRenderTime(e){return P(e,this.lastReportedTime)?(this.renderTime(this.lastReportedTime,e),!0):(this.lastReportedTime=e,!1)}}class A{constructor(e,t,r){this.entries=e,this.timeTracker=t,this.logbookEntries=r,_(this,"curIndex",void 0),_(this,"pendingItems",[]),this.curIndex=r.length>0&&"automation"===r[0].domain?1:0}get curItem(){return this.logbookEntries[this.curIndex]}get hasNext(){return this.curIndex<this.logbookEntries.length}maybeRenderItem(){const e=this.curItem;this.curIndex++;const t=new Date(1e3*e.when);if(0===this.pendingItems.length)return void this.pendingItems.push([t,e]);const r=this.pendingItems[this.pendingItems.length-1][0];P(r,t)&&(this._renderLogbookEntries(),this.timeTracker.renderTime(r,t)),this.pendingItems.push([t,e])}flush(){this.pendingItems.length>0&&this._renderLogbookEntries()}_renderLogbookEntries(){this.timeTracker.maybeRenderTime(this.pendingItems[0][0]);const e=[];let r,i;for(r=0;r<Math.min(this.pendingItems.length,2);r++)e.push(this._renderLogbookEntryHelper(this.pendingItems[r][1]));if(r<this.pendingItems.length)for(i=[];r<this.pendingItems.length;r++)i.push(this._renderLogbookEntryHelper(this.pendingItems[r][1]));this.entries.push(t.dy`
      <ha-timeline .icon=${"M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"} .moreItems=${i}>
        ${e}
      </ha-timeline>
    `),this.timeTracker.setLastReportedTime(this.pendingItems[this.pendingItems.length-1][0]),this.pendingItems=[]}_renderLogbookEntryHelper(e){return t.dy`${e.name} (${e.entity_id})
      ${e.message||`turned ${e.state}`}<br />`}}class D{constructor(e,t,r,i,n){this.hass=e,this.entries=t,this.trace=r,this.logbookRenderer=i,this.timeTracker=n,_(this,"curIndex",0),_(this,"keys",void 0),this.keys=Object.keys(r.trace)}get curItem(){return this._getItem(this.curIndex)}get hasNext(){return this.curIndex<this.keys.length}renderItem(){this.curIndex=this._renderItem(this.curIndex)}_getItem(e){return this.trace.trace[this.keys[e]]}_renderItem(e,t,r){const i=this._getItem(e);if(r){let r;return i.forEach((i=>{r=this._renderIteration(e,i,t)})),r}return this._renderIteration(e,i[0],t)}_renderIteration(e,t,r){if((0,h.Zm)(t.path))return this._handleTrigger(e,t);const i=new Date(t.timestamp);for(;this.logbookRenderer.hasNext&&new Date(1e3*this.logbookRenderer.curItem.when)<i;)this.logbookRenderer.maybeRenderItem();this.logbookRenderer.flush(),this.timeTracker.maybeRenderTime(i);const n=t.path;let o;try{o=(0,h.nV)(this.trace.config,n)}catch(t){return this._renderEntry(n,`Unable to extract path ${n}. Download trace and report as bug`),e+1}const a=n.split("/");if(!(2===a.length)&&!r)return this._renderEntry(n,n.replace(/\//g," ")),e+1;if(r||(r=(0,c.Pw)(o)),"choose"===r)return this._handleChoose(e);if("repeat"===r)return this._handleRepeat(e);if("if"===r)return this._handleIf(e);if("parallel"===r)return this._handleParallel(e);this._renderEntry(n,(0,d.Q)(this.hass,o,r),void 0,!1===o.enabled);let s=e+1;for(;s<this.keys.length&&this.keys[s].split("/").length!==a.length;s++);return s}_handleTrigger(e,t){return this._renderEntry(t.path,`Triggered ${"trigger"===t.path?"manually":`by the ${this.trace.trigger}`} at\n    ${(0,o.E8)(new Date(t.timestamp),this.hass.locale)}`,x),e+1}_handleChoose(e){var t;const r=this.keys[e],i=r.split("/").length,n=this._getItem(e)[0],o="default"===(null===(t=n.result)||void 0===t?void 0:t.choice),a=this._getDataFromPath(this.keys[e]),s=!1===a.enabled,l=a.alias||"Choose";if(o)this._renderEntry(r,`${l}: Default action executed`,void 0,s);else if(n.result){const t="default"!==n.result.choice?n.result.choice+1:void 0,i=this._getDataFromPath(`${this.keys[e]}/choose/${n.result.choice}`),o=i?`${i.alias||`Option ${t}`} executed`:`Error: ${n.error}`;this._renderEntry(r,`${l}: ${o}`,void 0,s)}else this._renderEntry(r,`${l}: No action taken`,void 0,s);let d;for(d=e+1;d<this.keys.length;d++){const e=this.keys[d].split("/");if(e.length<=i)return d;if(o&&"default"===e[i+1]||!o&&"sequence"===e[i+3])break}for(;d<this.keys.length;){const e=this.keys[d];if(e.split("/").length<=i)return d;d=this._renderItem(d,(0,c.Pw)(this._getDataFromPath(e)))}return d}_handleRepeat(e){const t=this.keys[e],r=t.split("/").length,i=this._getDataFromPath(this.keys[e]),n=!1===i.enabled,o=i.alias||(0,d.Q)(this.hass,i);let a;for(this._renderEntry(t,o,void 0,n),a=e+1;a<this.keys.length;a++){const e=this.keys[a];if(e.split("/").length<=r)return a;a=this._renderItem(a,(0,c.Pw)(this._getDataFromPath(e)),!0)}return a}_handleIf(e){var t;const r=this.keys[e],i=r.split("/").length,n=this._getItem(e)[0],o=this._getDataFromPath(this.keys[e]),a=!1===o.enabled,s=o.alias||"If";if(null!==(t=n.result)&&void 0!==t&&t.choice){const t=this._getDataFromPath(`${this.keys[e]}/${n.result.choice}/`),i=t?`${t.alias||`${n.result.choice} action executed`}`:`Error: ${n.error}`;this._renderEntry(r,`${s}: ${i}`,void 0,a)}else this._renderEntry(r,`${s}: No action taken`,void 0,a);let l;for(l=e+1;l<this.keys.length;l++){const e=this.keys[l],t=this.keys[l].split("/");if(t.length<=i)return l;"condition"===t[i+1]||t.length<i+2||(l=this._renderItem(l,(0,c.Pw)(this._getDataFromPath(e))))}return l}_handleParallel(e){const t=this.keys[e],r=t.split("/").length,i=this._getDataFromPath(this.keys[e]),n=!1===i.enabled,o=i.alias||"Execute in parallel";let a;for(this._renderEntry(t,o,void 0,n),a=e+1;a<this.keys.length;a++){const e=this.keys[a];if(e.split("/").length<=r)return a;a=this._renderItem(a,(0,c.Pw)(this._getDataFromPath(e)))}return a}_renderEntry(e,r,i="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9Z",n=!1){this.entries.push(t.dy`
      <ha-timeline .icon=${i} data-path=${e} .notEnabled=${n}>
        ${r}${n?t.dy`<span class="disabled"> (disabled)</span>`:""}
      </ha-timeline>
    `)}_getDataFromPath(e){return(0,h.nV)(this.trace.config,e)}}!function(e,t,r,i){var n=p();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(v(o.descriptor)||v(n.descriptor)){if(y(o)||y(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(y(o)){if(y(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}m(o,n)}else t.push(o)}return t}(a.d.map(f)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,i.Mo)("hat-trace-timeline")],(function(e,r){class a extends r{constructor(...t){super(...t),e(this)}}return{F:a,d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"trace",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"logbookEntries",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"selectedPath",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"allowPick",value:()=>!1},{kind:"method",key:"render",value:function(){if(!this.trace)return t.dy``;const e=[],r=new C(this.hass,e,this.trace),i=new A(e,r,this.logbookEntries||[]),a=new D(this.hass,e,this.trace,i,r);for(;a.hasNext;)a.renderItem();for(;i.hasNext;)i.maybeRenderItem();i.flush();const s=()=>(0,o.E8)(new Date(this.trace.timestamp.finish),this.hass.locale),l=()=>`(runtime:\n      ${((new Date(this.trace.timestamp.finish).getTime()-new Date(this.trace.timestamp.start).getTime())/1e3).toFixed(2)}\n      seconds)`;let c;if("running"===this.trace.state)c={description:"Still running",icon:"M13,2.03V2.05L13,4.05C17.39,4.59 20.5,8.58 19.96,12.97C19.5,16.61 16.64,19.5 13,19.93V21.93C18.5,21.38 22.5,16.5 21.95,11C21.5,6.25 17.73,2.5 13,2.03M11,2.06C9.05,2.25 7.19,3 5.67,4.26L7.1,5.74C8.22,4.84 9.57,4.26 11,4.06V2.06M4.26,5.67C3,7.19 2.25,9.04 2.05,11H4.05C4.24,9.58 4.8,8.23 5.69,7.1L4.26,5.67M2.06,13C2.26,14.96 3.03,16.81 4.27,18.33L5.69,16.9C4.81,15.77 4.24,14.42 4.06,13H2.06M7.1,18.37L5.67,19.74C7.18,21 9.04,21.79 11,22V20C9.58,19.82 8.23,19.25 7.1,18.37M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z"};else if("debugged"===this.trace.state)c={description:"Debugged",icon:"M13,2.03V2.05L13,4.05C17.39,4.59 20.5,8.58 19.96,12.97C19.5,16.61 16.64,19.5 13,19.93V21.93C18.5,21.38 22.5,16.5 21.95,11C21.5,6.25 17.73,2.5 13,2.03M11,2.06C9.05,2.25 7.19,3 5.67,4.26L7.1,5.74C8.22,4.84 9.57,4.26 11,4.06V2.06M4.26,5.67C3,7.19 2.25,9.04 2.05,11H4.05C4.24,9.58 4.8,8.23 5.69,7.1L4.26,5.67M2.06,13C2.26,14.96 3.03,16.81 4.27,18.33L5.69,16.9C4.81,15.77 4.24,14.42 4.06,13H2.06M7.1,18.37L5.67,19.74C7.18,21 9.04,21.79 11,22V20C9.58,19.82 8.23,19.25 7.1,18.37M16.82,15.19L12.71,11.08C13.12,10.04 12.89,8.82 12.03,7.97C11.13,7.06 9.78,6.88 8.69,7.38L10.63,9.32L9.28,10.68L7.29,8.73C6.75,9.82 7,11.17 7.88,12.08C8.74,12.94 9.96,13.16 11,12.76L15.11,16.86C15.29,17.05 15.56,17.05 15.74,16.86L16.78,15.83C17,15.65 17,15.33 16.82,15.19Z"};else if("finished"===this.trace.script_execution)c={description:`Finished at ${s()} ${l()}`,icon:x};else if("aborted"===this.trace.script_execution)c={description:`Aborted at ${s()} ${l()}`,icon:$};else if("cancelled"===this.trace.script_execution)c={description:`Cancelled at ${s()} ${l()}`,icon:$};else{let e,r,i=!1;switch(this.trace.script_execution){case"failed_conditions":e="a condition failed";break;case"failed_single":e="only a single execution is allowed";break;case"failed_max_runs":e="maximum number of parallel runs reached";break;case"error":e="an error was encountered",i=!0,r=t.dy`<br /><br />${this.trace.error}`;break;default:e=`of unknown reason "${this.trace.script_execution}"`,i=!0}c={description:t.dy`Stopped because ${e} at ${s()}
        ${l()}${r||""}`,icon:$,className:i?"error":void 0}}return e.push(t.dy`
      <ha-timeline
        lastItem
        .icon=${c.icon}
        class=${(0,n.o)(c.className)}
      >
        ${c.description}
      </ha-timeline>
    `),t.dy`${e}`}},{kind:"method",key:"updated",value:function(e){if(w(E(a.prototype),"updated",this).call(this,e),this.allowPick&&e.has("trace")&&this.trace&&this.selectedPath&&!(this.selectedPath in this.trace.trace)){const e=this.shadowRoot.querySelector("ha-timeline[data-path]");e&&((0,s.B)(this,"value-changed",{value:e.dataset.path}),this.selectedPath=e.dataset.path)}(e.has("trace")||e.has("selectedPath"))&&this.shadowRoot.querySelectorAll("ha-timeline[data-path]").forEach((e=>{if((0,l.X)(e,"selected",this.selectedPath===e.dataset.path),!this.allowPick||0===e.tabIndex)return;e.tabIndex=0;const t=()=>{this.selectedPath=e.dataset.path,(0,s.B)(this,"value-changed",{value:e.dataset.path})};e.addEventListener("click",t),e.addEventListener("keydown",(e=>{"Enter"!==e.key&&" "!==e.key||t()})),e.addEventListener("mouseover",(()=>{e.raised=!0})),e.addEventListener("mouseout",(()=>{e.raised=!1}))}))}},{kind:"get",static:!0,key:"styles",value:function(){return[t.iv`
        ha-timeline[lastItem].condition {
          --timeline-ball-color: var(--error-color);
        }
        ha-timeline[data-path] {
          cursor: pointer;
        }
        ha-timeline[selected] {
          --timeline-ball-color: var(--primary-color);
        }
        ha-timeline:focus {
          outline: none;
          --timeline-ball-color: var(--accent-color);
        }
        .error {
          --timeline-ball-color: var(--error-color);
          color: var(--error-color);
        }
      `]}}]}}),t.oi)}))},19476:(e,t,r)=>{r.d(t,{b:()=>i});const i=r(37500).iv`
  .tabs {
    background-color: var(--primary-background-color);
    border-top: 1px solid var(--divider-color);
    border-bottom: 1px solid var(--divider-color);
    display: flex;
    padding-left: 4px;
  }

  .tabs.top {
    border-top: none;
  }

  .tabs > * {
    padding: 2px 16px;
    cursor: pointer;
    position: relative;
    bottom: -1px;
    border: none;
    border-bottom: 2px solid transparent;
    user-select: none;
    background: none;
    color: var(--primary-text-color);
    outline: none;
    transition: background 15ms linear;
  }

  .tabs > *.active {
    border-bottom-color: var(--accent-color);
  }

  .tabs > *:focus,
  .tabs > *:hover {
    background: var(--secondary-background-color);
  }
`},55422:(e,t,r)=>{r.a(e,(async e=>{r.d(t,{jV:()=>d,sS:()=>p,Yc:()=>m,tf:()=>y,o1:()=>v,hb:()=>g,ri:()=>b,MY:()=>k});var i=r(49706),n=r(58831),o=r(29171),a=r(22311),s=r(56007),l=e([o]);o=(l.then?await l:l)[0];const c="ui.components.logbook.messages",d=["counter","proximity","sensor"],h={"numeric state of":"triggered_by_numeric_state_of","state of":"triggered_by_state_of",event:"triggered_by_event",time:"triggered_by_time","time pattern":"triggered_by_time_pattern","Home Assistant stopping":"triggered_by_homeassistant_stopping","Home Assistant starting":"triggered_by_homeassistant_starting"},u={},p=async(e,t,r)=>(await e.loadBackendTranslation("device_class"),f(e,t,void 0,void 0,r)),f=(e,t,r,i,n,o)=>{if((i||o)&&(!i||0===i.length)&&(!o||0===o.length))return Promise.resolve([]);const a={type:"logbook/get_events",start_time:t};return r&&(a.end_time=r),null!=i&&i.length&&(a.entity_ids=i),null!=o&&o.length&&(a.device_ids=o),n&&(a.context_id=n),e.callWS(a)},m=(e,t,r,i,n,o)=>{if((n||o)&&(!n||0===n.length)&&(!o||0===o.length))return Promise.reject("No entities or devices");const a={type:"logbook/event_stream",start_time:r,end_time:i};return null!=n&&n.length&&(a.entity_ids=n),null!=o&&o.length&&(a.device_ids=o),e.connection.subscribeMessage((e=>t(e)),a)},y=(e,t)=>{u[`${e}${t}`]={}},v=(e,t)=>({entity_id:e.entity_id,state:t,attributes:{device_class:null==e?void 0:e.attributes.device_class,source_type:null==e?void 0:e.attributes.source_type,has_date:null==e?void 0:e.attributes.has_date,has_time:null==e?void 0:e.attributes.has_time,entity_picture_local:i.iY.has((0,n.M)(e.entity_id))||null==e?void 0:e.attributes.entity_picture_local,entity_picture:i.iY.has((0,n.M)(e.entity_id))||null==e?void 0:e.attributes.entity_picture}}),g=(e,t)=>{for(const r in h)if(t.startsWith(r))return t.replace(r,`${e(`ui.components.logbook.${h[r]}`)}`);return t},b=(e,t,r,n,a)=>{switch(a){case"device_tracker":case"person":return"not_home"===r?t(`${c}.was_away`):"home"===r?t(`${c}.was_at_home`):t(`${c}.was_at_state`,"state",r);case"sun":return t("above_horizon"===r?`${c}.rose`:`${c}.set`);case"binary_sensor":{const e=r===i.uo,o=r===i.lC,a=n.attributes.device_class;switch(a){case"battery":if(e)return t(`${c}.was_low`);if(o)return t(`${c}.was_normal`);break;case"connectivity":if(e)return t(`${c}.was_connected`);if(o)return t(`${c}.was_disconnected`);break;case"door":case"garage_door":case"opening":case"window":if(e)return t(`${c}.was_opened`);if(o)return t(`${c}.was_closed`);break;case"lock":if(e)return t(`${c}.was_unlocked`);if(o)return t(`${c}.was_locked`);break;case"plug":if(e)return t(`${c}.was_plugged_in`);if(o)return t(`${c}.was_unplugged`);break;case"presence":if(e)return t(`${c}.was_at_home`);if(o)return t(`${c}.was_away`);break;case"safety":if(e)return t(`${c}.was_unsafe`);if(o)return t(`${c}.was_safe`);break;case"cold":case"gas":case"heat":case"moisture":case"motion":case"occupancy":case"power":case"problem":case"smoke":case"sound":case"vibration":if(e)return t(`${c}.detected_device_class`,{device_class:t(`component.binary_sensor.device_class.${a}`)});if(o)return t(`${c}.cleared_device_class`,{device_class:t(`component.binary_sensor.device_class.${a}`)});break;case"tamper":if(e)return t(`${c}.detected_tampering`);if(o)return t(`${c}.cleared_tampering`)}break}case"cover":switch(r){case"open":return t(`${c}.was_opened`);case"opening":return t(`${c}.is_opening`);case"closing":return t(`${c}.is_closing`);case"closed":return t(`${c}.was_closed`)}break;case"lock":if("unlocked"===r)return t(`${c}.was_unlocked`);if("locked"===r)return t(`${c}.was_locked`)}return r===i.uo?t(`${c}.turned_on`):r===i.lC?t(`${c}.turned_off`):s.V_.includes(r)?t(`${c}.became_unavailable`):e.localize(`${c}.changed_to_state`,"state",n?(0,o.D)(t,n,e.locale,r):r)},k=e=>"sensor"!==(0,a.N)(e)||void 0===e.attributes.unit_of_measurement&&void 0===e.attributes.state_class}))},59847:(e,t,r)=>{r.d(t,{Q:()=>c});var i=r(91168),n=r(42141),o=r(91741),a=r(61761);const s=e=>e.alias?e.alias:["or","and","not"].includes(e.condition)?`multiple conditions using "${e.condition}"`:`${e.condition} condition`;var l=r(44547);const c=(e,t,r)=>{if(t.alias)return t.alias;if(r||(r=(0,l.Pw)(t)),"service"===r){const e=t;let i;if(e.service_template||e.service&&(0,a.J)(e.service))i="Call a service based on a template";else{if(!e.service)return r;i=`Call service ${e.service}`}if(e.target){const t=[];for(const[r,i]of Object.entries({area_id:"areas",device_id:"devices",entity_id:"entities"})){if(!(r in e.target))continue;const n=Array.isArray(e.target[r])?e.target[r]:[e.target[r]],o=[];let s=!0;for(const e of n){if((0,a.J)(e)){t.push(`templated ${i}`),s=!1;break}o.push(e)}s&&t.push(`${i} ${o.join(", ")}`)}t.length>0&&(i+=` on ${t.join(", ")}`)}return i}if("delay"===r){const e=t;let r;return r="number"==typeof e.delay?`for ${(0,i.Z)(e.delay)}`:"string"==typeof e.delay?(0,a.J)(e.delay)?"based on a template":`for ${e.delay}`:`for ${JSON.stringify(e.delay)}`,`Delay ${r}`}if("activate_scene"===r){var d;const r=t;let i;var h;if("scene"in r)i=r.scene;else i=(null===(h=r.target)||void 0===h?void 0:h.entity_id)||r.entity_id;const n=i?e.states[i]:void 0;return`Activate scene ${n?(0,o.C)(n):"scene"in r?r.scene:(null===(d=r.target)||void 0===d?void 0:d.entity_id)||r.entity_id}`}if("play_media"===r){var u,p;const r=t,i=(null===(u=r.target)||void 0===u?void 0:u.entity_id)||r.entity_id,n=i?e.states[i]:void 0;return`Play ${r.metadata.title||r.data.media_content_id} on ${n?(0,o.C)(n):(null===(p=r.target)||void 0===p?void 0:p.entity_id)||r.entity_id}`}if("wait_for_trigger"===r){const e=t;return`Wait for ${(0,n.r)(e.wait_for_trigger).map((e=>(e=>`${e.platform} trigger`)(e))).join(", ")}`}if("variables"===r){const e=t;return`Define variables ${Object.keys(e.variables).join(", ")}`}if("fire_event"===r){const e=t;return(0,a.J)(e.event)?"Fire event based on a template":`Fire event ${e.event}`}if("wait_template"===r)return"Wait for a template to render true";if("check_condition"===r)return`Test ${s(t)}`;if("stop"===r){const e=t;return"Stopped"+(e.stop?` because: ${e.stop}`:"")}if("if"===r){const r=t;return`If ${"string"==typeof r.if?r.if:(0,n.r)(r.if).map((e=>s(e))).join(", ")} then ${(0,n.r)(r.then).map((t=>c(e,t)))}${r.else?` else ${(0,n.r)(r.else).map((t=>c(e,t)))}`:""}`}if("choose"===r){const r=t;return r.choose?`If ${(0,n.r)(r.choose).map((t=>`${"string"==typeof t.conditions?t.conditions:(0,n.r)(t.conditions).map((e=>s(e))).join(", ")} then ${(0,n.r)(t.sequence).map((t=>c(e,t))).join(", ")}`)).join(", else if ")}${r.default?`. If none match: ${(0,n.r)(r.default).map((t=>c(e,t))).join(", ")}`:""}`:"Choose"}if("repeat"===r){const r=t;return`Repeat ${(0,n.r)(r.repeat.sequence).map((t=>c(e,t)))} ${"count"in r.repeat?`${r.repeat.count} times`:""}${"while"in r.repeat?`while ${(0,n.r)(r.repeat.while).map((e=>s(e))).join(", ")} is true`:"until"in r.repeat?`until ${(0,n.r)(r.repeat.until).map((e=>s(e))).join(", ")} is true`:"for_each"in r.repeat?`for every item: ${(0,n.r)(r.repeat.for_each).map((e=>JSON.stringify(e))).join(", ")}`:""}`}if("check_condition"===r)return`Test ${s(t)}`;if("device_action"===r){const r=t,i=e.states[r.entity_id];return`${r.type||"Perform action with"} ${i?(0,o.C)(i):r.entity_id}`}if("parallel"===r){const r=t;return`Run in parallel: ${(0,n.r)(r.parallel).map((t=>c(e,t))).join(", ")}`}return r}},97389:(e,t,r)=>{r.d(t,{mA:()=>n,lj:()=>o,U_:()=>a,nV:()=>s,Zm:()=>l});var i=r(43793);const n=(e,t,r,i)=>e.callWS({type:"trace/get",domain:t,item_id:r,run_id:i}),o=(e,t,r)=>e.callWS({type:"trace/list",domain:t,item_id:r}),a=(e,t,r)=>e.callWS({type:"trace/contexts",domain:t,item_id:r}),s=(e,t)=>{const r=t.split("/").reverse();let i=e;for(;r.length;){const e=r.pop(),t=Number(e);if(isNaN(t)){const t=i[e];if(!t&&"sequence"===e)continue;i=t}else if(Array.isArray(i))i=i[t];else if(0!==t)throw new Error("If config is not an array, can only return index 0")}return i},l=e=>"trigger"===e||(0,i.x)(e,"trigger/")},44198:(e,t,r)=>{r.a(e,(async e=>{r(9874);var t=r(37500),i=r(33310),n=r(8636),o=r(12198),a=r(49684),s=r(25516),l=r(47181),c=r(58831),d=r(7323),h=(r(3143),r(31206),r(42952)),u=r(55422),p=r(11654),f=r(11254),m=e([u,a,o,h]);function y(){y=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!b(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return _(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?_(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=E(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:w(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=w(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function v(e){var t,r=E(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function g(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function b(e){return e.decorators&&e.decorators.length}function k(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function w(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function E(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function _(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}[u,a,o,h]=m.then?await m:m;const $=["script","automation"];!function(e,t,r,i){var n=y();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(k(o.descriptor)||k(n.descriptor)){if(b(o)||b(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(b(o)){if(b(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}g(o,n)}else t.push(o)}return t}(a.d.map(v)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,i.Mo)("ha-logbook-renderer")],(function(e,r){return{F:class extends r{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"userIdToName",value:()=>({})},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"traceContexts",value:()=>({})},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"entries",value:()=>[]},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,attribute:"narrow"})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,attribute:"virtualize",reflect:!0})],key:"virtualize",value:()=>!1},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,attribute:"no-icon"})],key:"noIcon",value:()=>!1},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,attribute:"no-name"})],key:"noName",value:()=>!1},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,attribute:"relative-time"})],key:"relativeTime",value:()=>!1},{kind:"field",decorators:[(0,s.i)(".container")],key:"_savedScrollPos",value:void 0},{kind:"method",key:"shouldUpdate",value:function(e){const t=e.get("hass"),r=void 0===t||t.locale!==this.hass.locale;return e.has("entries")||e.has("traceContexts")||r}},{kind:"method",key:"render",value:function(){var e;return null!==(e=this.entries)&&void 0!==e&&e.length?t.dy`
      <div
        class="container ha-scrollbar ${(0,n.$)({narrow:this.narrow,"no-name":this.noName,"no-icon":this.noIcon})}"
        @scroll=${this._saveScrollPos}
      >
        ${this.virtualize?t.dy`<lit-virtualizer
              @visibilityChanged=${this._visibilityChanged}
              scroller
              class="ha-scrollbar"
              .items=${this.entries}
              .renderItem=${this._renderLogbookItem}
            >
            </lit-virtualizer>`:this.entries.map(((e,t)=>this._renderLogbookItem(e,t)))}
      </div>
    `:t.dy`
        <div class="container no-entries">
          ${this.hass.localize("ui.components.logbook.entries_not_found")}
        </div>
      `}},{kind:"field",key:"_renderLogbookItem",value(){return(e,r)=>{var i;if(!e||void 0===r)return t.dy``;const s=this.entries[r-1],l=[],h=e.entity_id?this.hass.states[e.entity_id]:void 0,p=h?(0,u.o1)(h,e.state):void 0,m=e.entity_id?(0,c.M)(e.entity_id):e.domain,y=p||e.icon||e.state||!m||!(0,d.p)(this.hass,m)?void 0:(0,f.X1)({domain:m,type:"icon",useFallback:!0,darkOptimized:null===(i=this.hass.themes)||void 0===i?void 0:i.darkMode});return t.dy`
      <div class="entry-container">
        ${0===r||null!=e&&e.when&&null!=s&&s.when&&new Date(1e3*e.when).toDateString()!==new Date(1e3*s.when).toDateString()?t.dy`
              <h4 class="date">
                ${(0,o.p6)(new Date(1e3*e.when),this.hass.locale)}
              </h4>
            `:t.dy``}

        <div class="entry ${(0,n.$)({"no-entity":!e.entity_id})}">
          <div class="icon-message">
            ${this.noIcon?"":t.dy`
                  <state-badge
                    .hass=${this.hass}
                    .overrideIcon=${e.icon}
                    .overrideImage=${y}
                    .stateObj=${e.icon?void 0:p}
                    .stateColor=${!1}
                  ></state-badge>
                `}
            <div class="message-relative_time">
              <div class="message">
                ${this.noName?"":this._renderEntity(e.entity_id,e.name)}
                ${this._renderMessage(e,l,m,p)}
                ${this._renderContextMessage(e,l)}
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
                ${e.context_user_id?t.dy`${this._renderUser(e)}`:""}
                ${$.includes(e.domain)&&e.context_id in this.traceContexts?t.dy`
                      -
                      <a
                        href=${`/config/${this.traceContexts[e.context_id].domain}/trace/${"script"===this.traceContexts[e.context_id].domain?`script.${this.traceContexts[e.context_id].item_id}`:this.traceContexts[e.context_id].item_id}?run_id=${this.traceContexts[e.context_id].run_id}`}
                        @click=${this._close}
                        >${this.hass.localize("ui.components.logbook.show_trace")}</a
                      >
                    `:""}
              </div>
            </div>
          </div>
        </div>
      </div>
    `}}},{kind:"method",decorators:[(0,i.hO)({passive:!0})],key:"_saveScrollPos",value:function(e){this._savedScrollPos=e.target.scrollTop}},{kind:"method",decorators:[(0,i.hO)({passive:!0})],key:"_visibilityChanged",value:function(e){(0,l.B)(this,"hass-logbook-live",{enable:0===e.first})}},{kind:"method",key:"_renderMessage",value:function(e,t,r,i){if(e.entity_id&&e.state)return i?(0,u.ri)(this.hass,this.hass.localize,e.state,i,r):e.state;const n=(e=>e.context_event_type||e.context_state||e.context_message)(e);let o=e.message;if($.includes(r)&&e.source){if(n)return"";o=(0,u.hb)(this.hass.localize,e.source)}return o?this._formatMessageWithPossibleEntity(n?((e,t)=>t?e.replace(t," "):e)(o,e.context_entity_id):o,t,void 0):""}},{kind:"method",key:"_renderUser",value:function(e){const t=e.context_user_id&&this.userIdToName[e.context_user_id];return t?`- ${t}`:""}},{kind:"method",key:"_renderUnseenContextSourceEntity",value:function(e,r){return!e.context_entity_id||r.includes(e.context_entity_id)?"":t.dy` (${this._renderEntity(e.context_entity_id,e.context_entity_id_name)})`}},{kind:"method",key:"_renderContextMessage",value:function(e,r){if(e.context_state){const r=e.context_entity_id&&e.context_entity_id in this.hass.states?(0,u.o1)(this.hass.states[e.context_entity_id],e.context_state):void 0;return t.dy`${this.hass.localize("ui.components.logbook.triggered_by_state_of")}
      ${this._renderEntity(e.context_entity_id,e.context_entity_id_name)}
      ${r?(0,u.ri)(this.hass,this.hass.localize,e.context_state,r,(0,c.M)(e.context_entity_id)):e.context_state}`}if("call_service"===e.context_event_type)return t.dy`${this.hass.localize("ui.components.logbook.triggered_by_service")}
      ${e.context_domain}.${e.context_service}`;if(!e.context_message||r.includes(e.context_entity_id))return"";if("automation_triggered"===e.context_event_type||"script_started"===e.context_event_type){const i=e.context_source?e.context_source:e.context_message.replace("triggered by ",""),n=(0,u.hb)(this.hass.localize,i);return t.dy`${this.hass.localize("automation_triggered"===e.context_event_type?"ui.components.logbook.triggered_by_automation":"ui.components.logbook.triggered_by_script")}
      ${this._renderEntity(e.context_entity_id,e.context_entity_id_name)}
      ${e.context_message?this._formatMessageWithPossibleEntity(n,r):""}`}return t.dy` ${this.hass.localize("ui.components.logbook.triggered_by")}
    ${e.context_name}
    ${this._formatMessageWithPossibleEntity(e.context_message,r,e.context_entity_id)}
    ${this._renderUnseenContextSourceEntity(e,r)}`}},{kind:"method",key:"_renderEntity",value:function(e,r){const i=e&&e in this.hass.states,n=r||i&&this.hass.states[e].attributes.friendly_name||e;return i?t.dy`<button
      class="link"
      @click=${this._entityClicked}
      .entityId=${e}
    >
      ${n}
    </button>`:n}},{kind:"method",key:"_formatMessageWithPossibleEntity",value:function(e,r,i){if(-1!==e.indexOf(".")){const i=e.split(" ");for(let e=0,n=i.length;e<n;e++)if(i[e]in this.hass.states){const n=i[e];if(r.includes(n))return"";r.push(n);const o=i.splice(e);return o.shift(),t.dy`${i.join(" ")}
          ${this._renderEntity(n,this.hass.states[n].attributes.friendly_name)}
          ${o.join(" ")}`}}if(i&&i in this.hass.states){const n=this.hass.states[i].attributes.friendly_name;if(n&&e.endsWith(n))return r.includes(i)?"":(r.push(i),e=e.substring(0,e.length-n.length),t.dy`${e}
        ${this._renderEntity(i,n)}`)}return e}},{kind:"method",key:"_entityClicked",value:function(e){const t=e.currentTarget.entityId;t&&(e.preventDefault(),e.stopPropagation(),(0,l.B)(this,"hass-more-info",{entityId:t}))}},{kind:"method",key:"_close",value:function(){setTimeout((()=>(0,l.B)(this,"closed")),500)}},{kind:"get",static:!0,key:"styles",value:function(){return[p.Qx,p.$c,p.k1,t.iv`
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
        }

        .entry.no-entity,
        .no-name .entry {
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
          margin-inline-end: initial;
          direction: var(--direction);
        }
      `]}}]}}),t.oi)}))}}]);
//# sourceMappingURL=20cb68a9.js.map