"use strict";(self.webpackChunkreact_frontend=self.webpackChunkreact_frontend||[]).push([[5822],{99040:(e,t,i)=>{var r=i(97566),n=i(54281),o=i(26445),a=i(17871);function s(){s=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!d(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return m(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?m(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=u(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:p(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=p(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function l(e){var t,i=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function c(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function d(e){return e.decorators&&e.decorators.length}function h(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function p(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function f(){return f="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,i){var r=y(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},f.apply(this,arguments)}function y(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=v(e)););return e}function v(e){return v=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},v(e)}!function(e,t,i,r){var n=s();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=t((function(e){n.initializeInstanceElements(e,p.elements)}),i),p=n.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(h(o.descriptor)||h(n.descriptor)){if(d(o)||d(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(d(o)){if(d(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}c(o,n)}else t.push(o)}return t}(a.d.map(l)),e);n.initializeClassElements(a.F,p.elements),n.runClassFinishers(a.F,p.finishers)}([(0,o.Mo)("ha-fab")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"method",key:"firstUpdated",value:function(e){f(v(i.prototype),"firstUpdated",this).call(this,e),this.style.setProperty("--mdc-theme-secondary","var(--primary-color)")}},{kind:"field",static:!0,key:"styles",value:()=>[n.W,a.iv`
      :host .mdc-fab--extended .mdc-fab__icon {
        margin-inline-start: -8px;
        margin-inline-end: 12px;
        direction: var(--direction);
      }
    `,"rtl"===document.dir?a.iv`
          :host .mdc-fab--extended .mdc-fab__icon {
            direction: rtl;
          }
        `:a.iv``]}]}}),r._)},55822:(e,t,i)=>{i.r(t);i(95469);var r=i(72259),n=i(17871),o=i(26445),a=i(18394),s=i(51750),l=i(29950),c=(i(9828),i(82960),i(55398),i(37662),i(23469));function d(){d=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!u(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return v(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?v(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=y(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:f(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=f(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function h(e){var t,i=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function u(e){return e.decorators&&e.decorators.length}function m(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function f(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function v(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}!function(e,t,i,r){var n=d();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),i),s=n.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(m(o.descriptor)||m(n.descriptor)){if(u(o)||u(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(u(o)){if(u(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}p(o,n)}else t.push(o)}return t}(a.d.map(h)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,o.Mo)("ha-media-manage-button")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"currentItem",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_uploading",value:()=>0},{kind:"method",key:"render",value:function(){return this.currentItem&&(0,c.aV)(this.currentItem.media_content_id||"")?n.dy`
      <mwc-button
        .label=${this.hass.localize("ui.components.media-browser.file_management.manage")}
        @click=${this._manage}
      >
        <ha-svg-icon .path=${r.JO6} slot="icon"></ha-svg-icon>
      </mwc-button>
    `:n.dy``}},{kind:"method",key:"_manage",value:function(){var e,t;e=this,t={currentItem:this.currentItem,onClose:()=>(0,a.B)(this,"media-refresh")},(0,a.B)(e,"show-dialog",{dialogTag:"dialog-media-manage",dialogImport:()=>i.e(2429).then(i.bind(i,92429)),dialogParams:t})}},{kind:"field",static:!0,key:"styles",value:()=>n.iv`
    mwc-button {
      /* We use icon + text to show disabled state */
      --mdc-button-disabled-ink-color: --mdc-theme-primary;
    }

    ha-svg-icon[slot="icon"],
    ha-circular-progress[slot="icon"] {
      vertical-align: middle;
    }

    ha-svg-icon[slot="icon"] {
      margin-inline-start: 0px;
      margin-inline-end: 8px;
      direction: var(--direction);
    }
  `}]}}),n.oi);function g(){g=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!k(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return $(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?$(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=E(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:x(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=x(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function b(e){var t,i=E(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function w(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function k(e){return e.decorators&&e.decorators.length}function _(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function x(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function E(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function $(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}!function(e,t,i,r){var n=g();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),i),s=n.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(_(o.descriptor)||_(n.descriptor)){if(k(o)||k(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(k(o)){if(k(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}w(o,n)}else t.push(o)}return t}(a.d.map(b)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,o.Mo)("dialog-media-player-browse")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_currentItem",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_navigateIds",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.IO)("ha-media-player-browse")],key:"_browser",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._navigateIds=e.navigateIds||[{media_content_id:void 0,media_content_type:void 0}]}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,this._navigateIds=void 0,this._currentItem=void 0,(0,a.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){return this._params&&this._navigateIds?n.dy`
      <ha-dialog
        open
        scrimClickAction
        escapeKeyAction
        hideActions
        flexContent
        .heading=${this._currentItem?this._currentItem.title:this.hass.localize("ui.components.media-browser.media-player-browser")}
        @closed=${this.closeDialog}
      >
        <ha-header-bar slot="heading">
          ${this._navigateIds.length>1?n.dy`
                <ha-icon-button
                  slot="navigationIcon"
                  .path=${r.J3k}
                  @click=${this._goBack}
                ></ha-icon-button>
              `:""}
          <span slot="title">
            ${this._currentItem?this._currentItem.title:this.hass.localize("ui.components.media-browser.media-player-browser")}
          </span>

          <ha-media-manage-button
            slot="actionItems"
            .hass=${this.hass}
            .currentItem=${this._currentItem}
            @media-refresh=${this._refreshMedia}
          ></ha-media-manage-button>
          <ha-icon-button
            .label=${this.hass.localize("ui.dialogs.generic.close")}
            .path=${r.r5M}
            dialogAction="close"
            slot="actionItems"
            class="header_button"
            dir=${(0,s.Zu)(this.hass)}
          ></ha-icon-button>
        </ha-header-bar>
        <ha-media-player-browse
          dialog
          .hass=${this.hass}
          .entityId=${this._params.entityId}
          .navigateIds=${this._navigateIds}
          .action=${this._action}
          @close-dialog=${this.closeDialog}
          @media-picked=${this._mediaPicked}
          @media-browsed=${this._mediaBrowsed}
        ></ha-media-player-browse>
      </ha-dialog>
    `:n.dy``}},{kind:"method",key:"_goBack",value:function(){var e;this._navigateIds=null===(e=this._navigateIds)||void 0===e?void 0:e.slice(0,-1),this._currentItem=void 0}},{kind:"method",key:"_mediaBrowsed",value:function(e){this._navigateIds=e.detail.ids,this._currentItem=e.detail.current}},{kind:"method",key:"_mediaPicked",value:function(e){this._params.mediaPickedCallback(e.detail),"play"!==this._action&&this.closeDialog()}},{kind:"get",key:"_action",value:function(){return this._params.action||"play"}},{kind:"method",key:"_refreshMedia",value:function(){this._browser.refresh()}},{kind:"get",static:!0,key:"styles",value:function(){return[l.yu,n.iv`
        ha-dialog {
          --dialog-z-index: 8;
          --dialog-content-padding: 0;
        }

        ha-media-player-browse {
          --media-browser-max-height: calc(100vh - 65px);
          height: calc(100vh - 65px);
          direction: ltr;
        }

        @media (min-width: 800px) {
          ha-dialog {
            --mdc-dialog-max-width: 800px;
            --dialog-surface-position: fixed;
            --dialog-surface-top: 40px;
            --mdc-dialog-max-height: calc(100vh - 72px);
          }
          ha-media-player-browse {
            position: initial;
            --media-browser-max-height: 100vh - 137px;
            height: 100vh - 137px;
            width: 700px;
          }
        }

        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
          border-bottom: 1px solid var(--divider-color, rgba(0, 0, 0, 0.12));
        }

        ha-media-manage-button {
          --mdc-theme-primary: var(--mdc-theme-on-primary);
        }
      `]}}]}}),n.oi)},82960:(e,t,i)=>{i(58538);var r=i(44816),n=(i(55398),i(32419),i(47512),i(72259)),o=(i(28897),i(17871)),a=i(26445),s=i(66536),l=i(85142),c=i(73673),d=i(18394),h=i(51750),p=i(72218),u=i(92599),m=i(21157),f=i(78889),y=i(23469);const v="media-source://tts/";var g=i(11285),b=i(74096),w=i(29950),k=i(72824),_=i(84728),x=(i(91998),i(23860),i(85878),i(68336),i(84224),i(99040),i(50422),i(37662),i(32307));function E(e,t,i){return t in e?Object.defineProperty(e,t,{value:i,enumerable:!0,configurable:!0,writable:!0}):e[t]=i,e}class ${constructor(e=!0){E(this,"_storage",{}),E(this,"_listeners",{}),e&&window.addEventListener("storage",(e=>{e.key&&this.hasKey(e.key)&&(this._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,this._listeners[e.key]&&this._listeners[e.key].forEach((t=>t(e.oldValue?JSON.parse(e.oldValue):e.oldValue,this._storage[e.key]))))}))}addFromStorage(e){if(!this._storage[e]){const t=window.localStorage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}subscribeChanges(e,t){return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],()=>{this.unsubscribeChanges(e,t)}}unsubscribeChanges(e,t){if(!(e in this._listeners))return;const i=this._listeners[e].indexOf(t);-1!==i&&this._listeners[e].splice(i,1)}hasKey(e){return e in this._storage}getValue(e){return this._storage[e]}setValue(e,t){this._storage[e]=t;try{void 0===t?window.localStorage.removeItem(e):window.localStorage.setItem(e,JSON.stringify(t))}catch(e){}}}const z=new $,P=(e,t,i=!0,r)=>n=>{const o=i?z:new $(!1),a=String(n.key);e=e||String(n.key);const s=n.initializer?n.initializer():void 0;o.addFromStorage(e);const l=()=>o.hasKey(e)?o.getValue(e):s;return{kind:"method",placement:"prototype",key:n.key,descriptor:{set(i){((i,r)=>{let a;t&&(a=l()),o.setValue(e,r),t&&i.requestUpdate(n.key,a)})(this,i)},get:()=>l(),enumerable:!0,configurable:!0},finisher(s){if(t&&i){const t=s.prototype.connectedCallback,i=s.prototype.disconnectedCallback;s.prototype.connectedCallback=function(){var i;t.call(this),this[`__unbsubLocalStorage${a}`]=(i=this,o.subscribeChanges(e,(e=>{i.requestUpdate(n.key,e)})))},s.prototype.disconnectedCallback=function(){i.call(this),this[`__unbsubLocalStorage${a}`]()}}t&&s.createProperty(n.key,{noAccessor:!0,...r})}}};var C=i(86089);var O=i(28858),D=i(90642);const S=e=>{const t=[];if(!e)return t;const i=new Set;for(const[r]of e.languages){if(i.has(r))continue;i.add(r);let e=r;if(r in D.o.translations)e=D.o.translations[r].nativeName;else{const[t,i]=r.split("-");t in D.o.translations&&(e=`${D.o.translations[t].nativeName}`,t.toLowerCase()!==i.toLowerCase()&&(e+=` (${i})`))}t.push([r,e])}return t.sort(((e,t)=>(0,O.f)(e[1],t[1])))},I=(e,t,i)=>{const r=[];if(!t)return r;for(const[n,o]of t.languages)n===e&&r.push([o,i(`ui.panel.media-browser.tts.gender_${o}`)||i(`ui.panel.config.cloud.account.tts.${o}`)||o]);return r.sort(((e,t)=>(0,O.f)(e[1],t[1])))};i(71133),i(99539);function A(){A=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!F(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return M(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?M(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=H(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:B(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=B(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function T(e){var t,i=H(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function j(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function F(e){return e.decorators&&e.decorators.length}function R(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function B(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function H(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function M(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function U(){return U="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,i){var r=W(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},U.apply(this,arguments)}function W(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=N(e)););return e}function N(e){return N=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},N(e)}!function(e,t,i,r){var n=A();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),i),s=n.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(R(o.descriptor)||R(n.descriptor)){if(F(o)||F(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(F(o)){if(F(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}j(o,n)}else t.push(o)}return t}(a.d.map(T)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,a.Mo)("ha-browse-media-tts")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,a.Cb)()],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"item",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"action",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_cloudDefaultOptions",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_cloudOptions",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_cloudTTSInfo",value:void 0},{kind:"field",decorators:[P("cloudTtsTryMessage",!0,!1)],key:"_message",value:void 0},{kind:"method",key:"render",value:function(){var e;return o.dy`<ha-card>
      <div class="card-content">
        <ha-textarea
          autogrow
          .label=${this.hass.localize("ui.components.media-browser.tts.message")}
          .value=${this._message||this.hass.localize("ui.components.media-browser.tts.example_message",{name:(null===(e=this.hass.user)||void 0===e?void 0:e.name)||""})}
        >
        </ha-textarea>
        ${this._cloudDefaultOptions?this._renderCloudOptions():""}
      </div>
      <div class="card-actions">
        ${!this._cloudDefaultOptions||this._cloudDefaultOptions[0]===this._cloudOptions[0]&&this._cloudDefaultOptions[1]===this._cloudOptions[1]?o.dy`<span></span>`:o.dy`
              <button class="link" @click=${this._storeDefaults}>
                ${this.hass.localize("ui.components.media-browser.tts.set_as_default")}
              </button>
            `}

        <mwc-button @click=${this._ttsClicked}>
          ${this.hass.localize(`ui.components.media-browser.tts.action_${this.action}`)}
        </mwc-button>
      </div>
    </ha-card> `}},{kind:"method",key:"_renderCloudOptions",value:function(){if(!this._cloudTTSInfo||!this._cloudOptions)return"";const e=this.getLanguages(this._cloudTTSInfo),t=this._cloudOptions,i=this.getSupportedGenders(t[0],this._cloudTTSInfo,this.hass.localize);return o.dy`
      <div class="cloud-options">
        <ha-select
          fixedMenuPosition
          naturalMenuWidth
          .label=${this.hass.localize("ui.components.media-browser.tts.language")}
          .value=${t[0]}
          @selected=${this._handleLanguageChange}
          @closed=${C.U}
        >
          ${e.map((([e,t])=>o.dy`<mwc-list-item .value=${e}>${t}</mwc-list-item>`))}
        </ha-select>

        <ha-select
          fixedMenuPosition
          naturalMenuWidth
          .label=${this.hass.localize("ui.components.media-browser.tts.gender")}
          .value=${t[1]}
          @selected=${this._handleGenderChange}
          @closed=${C.U}
        >
          ${i.map((([e,t])=>o.dy`<mwc-list-item .value=${e}>${t}</mwc-list-item>`))}
        </ha-select>
      </div>
    `}},{kind:"method",key:"willUpdate",value:function(e){var t,r;if(U(N(i.prototype),"willUpdate",this).call(this,e),e.has("item")){if(this.item.media_content_id){const e=new URLSearchParams(this.item.media_content_id.split("?")[1]),t=e.get("message"),i=e.get("language"),r=e.get("gender");t&&(this._message=t),i&&r&&(this._cloudOptions=[i,r])}this.isCloudItem&&!this._cloudTTSInfo&&((r=this.hass,r.callWS({type:"cloud/tts/info"})).then((e=>{this._cloudTTSInfo=e})),(e=>e.callWS({type:"cloud/status"}))(this.hass).then((e=>{e.logged_in&&(this._cloudDefaultOptions=e.prefs.tts_default_voice,this._cloudOptions||(this._cloudOptions={...this._cloudDefaultOptions}))})))}if(e.has("message"))return;const n=null===(t=this.shadowRoot.querySelector("ha-textarea"))||void 0===t?void 0:t.value;void 0!==n&&n!==this._message&&(this._message=n)}},{kind:"method",key:"_handleLanguageChange",value:async function(e){e.target.value!==this._cloudOptions[0]&&(this._cloudOptions=[e.target.value,this._cloudOptions[1]])}},{kind:"method",key:"_handleGenderChange",value:async function(e){e.target.value!==this._cloudOptions[1]&&(this._cloudOptions=[this._cloudOptions[0],e.target.value])}},{kind:"field",key:"getLanguages",value:()=>(0,x.Z)(S)},{kind:"field",key:"getSupportedGenders",value:()=>(0,x.Z)(I)},{kind:"get",key:"isCloudItem",value:function(){return this.item.media_content_id.startsWith("media-source://tts/cloud")}},{kind:"method",key:"_ttsClicked",value:async function(){const e=this.shadowRoot.querySelector("ha-textarea").value;this._message=e;const t={...this.item},i=new URLSearchParams;i.append("message",e),this._cloudOptions&&(i.append("language",this._cloudOptions[0]),i.append("gender",this._cloudOptions[1])),t.media_content_id=`${t.media_content_id.split("?")[0]}?${i.toString()}`,t.can_play=!0,t.title=e,(0,d.B)(this,"tts-picked",{item:t})}},{kind:"method",key:"_storeDefaults",value:async function(){const e=this._cloudDefaultOptions;this._cloudDefaultOptions=[...this._cloudOptions];try{await(t=this.hass,i={tts_default_voice:this._cloudDefaultOptions},t.callWS({type:"cloud/update_prefs",...i}))}catch(t){this._cloudDefaultOptions=e,(0,g.Ys)(this,{text:this.hass.localize("ui.components.media-browser.tts.faild_to_store_defaults",{error:t.message||t})})}var t,i}},{kind:"field",static:!0,key:"styles",value:()=>[w.k1,o.iv`
      :host {
        margin: 16px auto;
        padding: 0 8px;
        display: flex;
        flex-direction: column;
        max-width: 400px;
      }
      .cloud-options {
        margin-top: 16px;
        display: flex;
        justify-content: space-between;
      }
      .cloud-options ha-select {
        width: 48%;
      }
      ha-textarea {
        width: 100%;
      }
      button.link {
        color: var(--primary-color);
      }
      .card-actions {
        display: flex;
        justify-content: space-between;
      }
    `]}]}}),o.oi);function V(){V=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var n=t.placement;if(t.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?e:i;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!G(e))return i.push(e);var t=this.decorateElement(e,n);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var o=this.decorateConstructor(i,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);i.push.apply(i,c)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return K(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?K(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=X(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:Z(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=Z(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function L(e){var t,i=X(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function q(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function G(e){return e.decorators&&e.decorators.length}function J(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function Z(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function X(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function K(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}function Q(){return Q="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,i){var r=Y(e,t);if(r){var n=Object.getOwnPropertyDescriptor(r,t);return n.get?n.get.call(arguments.length<3?e:i):n.value}},Q.apply(this,arguments)}function Y(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=ee(e)););return e}function ee(e){return ee=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},ee(e)}!function(e,t,i,r){var n=V();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),i),s=n.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var n,o=e[r];if("method"===o.kind&&(n=t.find(i)))if(J(o.descriptor)||J(n.descriptor)){if(G(o)||G(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(G(o)){if(G(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}q(o,n)}else t.push(o)}return t}(a.d.map(L)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,a.Mo)("ha-media-player-browse")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"entityId",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"action",value:()=>"play"},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"dialog",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)()],key:"navigateIds",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"narrow",reflect:!0})],key:"_narrow",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"scroll",reflect:!0})],key:"_scrolled",value:()=>!1},{kind:"field",decorators:[(0,a.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_parentItem",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_currentItem",value:void 0},{kind:"field",decorators:[(0,a.IO)(".header")],key:"_header",value:void 0},{kind:"field",decorators:[(0,a.IO)(".content")],key:"_content",value:void 0},{kind:"field",decorators:[(0,a.IO)("lit-virtualizer")],key:"_virtualizer",value:void 0},{kind:"field",key:"_observed",value:()=>!1},{kind:"field",key:"_headerOffsetHeight",value:()=>0},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"method",key:"connectedCallback",value:function(){Q(ee(i.prototype),"connectedCallback",this).call(this),this.updateComplete.then((()=>this._attachResizeObserver()))}},{kind:"method",key:"disconnectedCallback",value:function(){this._resizeObserver&&this._resizeObserver.disconnect()}},{kind:"method",key:"refresh",value:async function(){const e=this.navigateIds[this.navigateIds.length-1];try{this._currentItem=await this._fetchData(this.entityId,e.media_content_id,e.media_content_type),(0,d.B)(this,"media-browsed",{ids:this.navigateIds,current:this._currentItem})}catch(e){this._setError(e)}}},{kind:"method",key:"play",value:function(){var e;null!==(e=this._currentItem)&&void 0!==e&&e.can_play&&this._runAction(this._currentItem)}},{kind:"method",key:"willUpdate",value:function(e){var t;if(Q(ee(i.prototype),"willUpdate",this).call(this,e),e.has("entityId"))this._setError(void 0);else if(!e.has("navigateIds"))return;this._setError(void 0);const r=e.get("navigateIds"),n=this.navigateIds;null===(t=this._content)||void 0===t||t.scrollTo(0,0),this._scrolled=!1;const o=this._currentItem,a=this._parentItem;this._currentItem=void 0,this._parentItem=void 0;const s=n[n.length-1],l=n.length>1?n[n.length-2]:void 0;let c,h;e.has("entityId")||(r&&n.length===r.length+1&&r.every(((e,t)=>{const i=n[t];return i.media_content_id===e.media_content_id&&i.media_content_type===e.media_content_type}))?h=Promise.resolve(o):r&&n.length===r.length-1&&n.every(((e,t)=>{const i=r[t];return e.media_content_id===i.media_content_id&&e.media_content_type===i.media_content_type}))&&(c=Promise.resolve(a))),c||(c=this._fetchData(this.entityId,s.media_content_id,s.media_content_type)),c.then((e=>{this._currentItem=e,(0,d.B)(this,"media-browsed",{ids:n,current:e})}),(t=>{var i;r&&e.has("entityId")&&n.length===r.length&&r.every(((e,t)=>n[t].media_content_id===e.media_content_id&&n[t].media_content_type===e.media_content_type))?(0,d.B)(this,"media-browsed",{ids:[{media_content_id:void 0,media_content_type:void 0}],replace:!0}):"entity_not_found"===t.code&&m.V_.includes(null===(i=this.hass.states[this.entityId])||void 0===i?void 0:i.state)?this._setError({message:this.hass.localize("ui.components.media-browser.media_player_unavailable"),code:"entity_not_found"}):this._setError(t)})),h||void 0===l||(h=this._fetchData(this.entityId,l.media_content_id,l.media_content_type)),h&&h.then((e=>{this._parentItem=e}))}},{kind:"method",key:"shouldUpdate",value:function(e){if(e.size>1||!e.has("hass"))return!0;const t=e.get("hass");return void 0===t||t.localize!==this.hass.localize}},{kind:"method",key:"firstUpdated",value:function(){this._measureCard(),this._attachResizeObserver()}},{kind:"method",key:"updated",value:function(e){if(Q(ee(i.prototype),"updated",this).call(this,e),e.has("_scrolled"))this._animateHeaderHeight();else if(e.has("_currentItem")){var t;if(this._setHeaderHeight(),this._observed)return;const e=null===(t=this._virtualizer)||void 0===t?void 0:t._virtualizer;e&&(this._observed=!0,setTimeout((()=>e._observeMutations()),0))}}},{kind:"method",key:"render",value:function(){if(this._error)return o.dy`
        <div class="container">
          <ha-alert alert-type="error">
            ${this._renderError(this._error)}
          </ha-alert>
        </div>
      `;if(!this._currentItem)return o.dy`<ha-circular-progress active></ha-circular-progress>`;const e=this._currentItem,t=this.hass.localize(`ui.components.media-browser.class.${e.media_class}`),i=e.children||[],a=f.Fn[e.media_class],d=e.children_media_class?f.Fn[e.children_media_class]:f.Fn.directory,p=e.thumbnail?this._getSignedThumbnail(e.thumbnail).then((e=>`url(${e})`)):"none";return o.dy`
              ${e.can_play?o.dy`
                      <div
                        class="header ${(0,s.$)({"no-img":!e.thumbnail,"no-dialog":!this.dialog})}"
                        @transitionend=${this._setHeaderHeight}
                      >
                        <div class="header-content">
                          ${e.thumbnail?o.dy`
                                <div
                                  class="img"
                                  style="background-image: ${(0,c.C)(p,"")}"
                                >
                                  ${this._narrow&&null!=e&&e.can_play?o.dy`
                                        <ha-fab
                                          mini
                                          .item=${e}
                                          @click=${this._actionClicked}
                                        >
                                          <ha-svg-icon
                                            slot="icon"
                                            .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                            .path=${"play"===this.action?n._86:n.qX5}
                                          ></ha-svg-icon>
                                          ${this.hass.localize(`ui.components.media-browser.${this.action}`)}
                                        </ha-fab>
                                      `:""}
                                </div>
                              `:o.dy``}
                          <div class="header-info">
                            <div class="breadcrumb">
                              <h1 class="title">${e.title}</h1>
                              ${t?o.dy` <h2 class="subtitle">${t}</h2> `:""}
                            </div>
                            ${!e.can_play||e.thumbnail&&this._narrow?"":o.dy`
                                  <mwc-button
                                    raised
                                    .item=${e}
                                    @click=${this._actionClicked}
                                  >
                                    <ha-svg-icon
                                      .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                      .path=${"play"===this.action?n._86:n.qX5}
                                    ></ha-svg-icon>
                                    ${this.hass.localize(`ui.components.media-browser.${this.action}`)}
                                  </mwc-button>
                                `}
                          </div>
                        </div>
                      </div>
                    `:""}
          <div
            class="content"
            @scroll=${this._scroll}
            @touchmove=${this._scroll}
          >
            ${this._error?o.dy`
                    <div class="container">
                      <ha-alert alert-type="error">
                        ${this._renderError(this._error)}
                      </ha-alert>
                    </div>
                  `:(u=e.media_content_id,u.startsWith(v)?o.dy`
                    <ha-browse-media-tts
                      .item=${e}
                      .hass=${this.hass}
                      .action=${this.action}
                      @tts-picked=${this._ttsPicked}
                    ></ha-browse-media-tts>
                  `:i.length||e.not_shown?"grid"===d.layout?o.dy`
                    <lit-virtualizer
                      scroller
                      .layout=${(0,r.e)({itemSize:{width:"175px",height:"portrait"===d.thumbnail_ratio?"312px":"225px"},gap:"16px",flex:{preserve:"aspect-ratio"},justify:"space-evenly",direction:"vertical"})}
                      .items=${i}
                      .renderItem=${this._renderGridItem}
                      class="children ${(0,s.$)({portrait:"portrait"===d.thumbnail_ratio,not_shown:!!e.not_shown})}"
                    ></lit-virtualizer>
                    ${e.not_shown?o.dy`
                          <div class="grid not-shown">
                            <div class="title">
                              ${this.hass.localize("ui.components.media-browser.not_shown",{count:e.not_shown})}
                            </div>
                          </div>
                        `:""}
                  `:o.dy`
                    <mwc-list>
                      <lit-virtualizer
                        scroller
                        .items=${i}
                        style=${(0,l.V)({height:72*i.length+26+"px"})}
                        .renderItem=${this._renderListItem}
                      ></lit-virtualizer>
                      ${e.not_shown?o.dy`
                            <mwc-list-item
                              noninteractive
                              class="not-shown"
                              .graphic=${a.show_list_images?"medium":"avatar"}
                              dir=${(0,h.Zu)(this.hass)}
                            >
                              <span class="title">
                                ${this.hass.localize("ui.components.media-browser.not_shown",{count:e.not_shown})}
                              </span>
                            </mwc-list-item>
                          `:""}
                    </mwc-list>
                  `:o.dy`
                    <div class="container no-items">
                      ${"media-source://media_source/local/."===e.media_content_id?o.dy`
                            <div class="highlight-add-button">
                              <span>
                                <ha-svg-icon
                                  .path=${n._iZ}
                                ></ha-svg-icon>
                              </span>
                              <span>
                                ${this.hass.localize("ui.components.media-browser.file_management.highlight_button")}
                              </span>
                            </div>
                          `:this.hass.localize("ui.components.media-browser.no_items")}
                    </div>
                  `)}
          </div>
        </div>
      </div>
    `;var u}},{kind:"field",key:"_renderGridItem",value(){return e=>{const t=e.thumbnail?this._getSignedThumbnail(e.thumbnail).then((e=>`url(${e})`)):"none";return o.dy`
      <div class="child" .item=${e} @click=${this._childClicked}>
        <ha-card outlined>
          <div class="thumbnail">
            ${e.thumbnail?o.dy`
                  <div
                    class="${["app","directory"].includes(e.media_class)?"centered-image":""} ${(0,k.zC)(e.thumbnail)?"brand-image":""} image"
                    style="background-image: ${(0,c.C)(t,"")}"
                  ></div>
                `:o.dy`
                  <div class="icon-holder image">
                    <ha-svg-icon
                      class="folder"
                      .path=${f.Fn["directory"===e.media_class&&e.children_media_class||e.media_class].icon}
                    ></ha-svg-icon>
                  </div>
                `}
            ${e.can_play?o.dy`
                  <ha-icon-button
                    class="play ${(0,s.$)({can_expand:e.can_expand})}"
                    .item=${e}
                    .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                    .path=${"play"===this.action?n._86:n.qX5}
                    @click=${this._actionClicked}
                  ></ha-icon-button>
                `:""}
          </div>
          <div class="title">
            ${e.title}
            <paper-tooltip fitToVisibleBounds position="top" offset="4"
              >${e.title}</paper-tooltip
            >
          </div>
        </ha-card>
      </div>
    `}}},{kind:"field",key:"_renderListItem",value(){return e=>{const t=this._currentItem,i=f.Fn[t.media_class],r=i.show_list_images&&e.thumbnail?this._getSignedThumbnail(e.thumbnail).then((e=>`url(${e})`)):"none";return o.dy`
      <mwc-list-item
        @click=${this._childClicked}
        .item=${e}
        .graphic=${i.show_list_images?"medium":"avatar"}
        dir=${(0,h.Zu)(this.hass)}
      >
        <div
          class=${(0,s.$)({graphic:!0,thumbnail:!0===i.show_list_images})}
          style="background-image: ${(0,c.C)(r,"")}"
          slot="graphic"
        >
          <ha-icon-button
            class="play ${(0,s.$)({show:!i.show_list_images||!e.thumbnail})}"
            .item=${e}
            .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
            .path=${"play"===this.action?n._86:n.qX5}
            @click=${this._actionClicked}
          ></ha-icon-button>
        </div>
        <span class="title">${e.title}</span>
      </mwc-list-item>
    `}}},{kind:"method",key:"_getSignedThumbnail",value:async function(e){if(!e)return"";if(e.startsWith("/"))return(await(0,u.iI)(this.hass,e)).path;var t;(0,k.zC)(e)&&(e=(0,k.X1)({domain:(0,k.u4)(e),type:"icon",useFallback:!0,darkOptimized:null===(t=this.hass.themes)||void 0===t?void 0:t.darkMode}));return e}},{kind:"field",key:"_actionClicked",value(){return e=>{e.stopPropagation();const t=e.currentTarget.item;this._runAction(t)}}},{kind:"method",key:"_runAction",value:function(e){(0,d.B)(this,"media-picked",{item:e,navigateIds:this.navigateIds})}},{kind:"method",key:"_ttsPicked",value:function(e){e.stopPropagation();const t=this.navigateIds.slice(0,-1);t.push(e.detail.item),(0,d.B)(this,"media-picked",{...e.detail,navigateIds:t})}},{kind:"field",key:"_childClicked",value(){return async e=>{const t=e.currentTarget.item;t&&(t.can_expand?(0,d.B)(this,"media-browsed",{ids:[...this.navigateIds,t]}):this._runAction(t))}}},{kind:"method",key:"_fetchData",value:async function(e,t,i){return e!==f.N8?(0,f.zz)(this.hass,e,t,i):(0,y.b)(this.hass,t)}},{kind:"method",key:"_measureCard",value:function(){this._narrow=(this.dialog?window.innerWidth:this.offsetWidth)<450}},{kind:"method",key:"_attachResizeObserver",value:async function(){this._resizeObserver||(await(0,b.P)(),this._resizeObserver=new ResizeObserver((0,p.D)((()=>this._measureCard()),250,!1))),this._resizeObserver.observe(this)}},{kind:"method",key:"_closeDialogAction",value:function(){(0,d.B)(this,"close-dialog")}},{kind:"method",key:"_setError",value:function(e){this.dialog?e&&(this._closeDialogAction(),(0,g.Ys)(this,{title:this.hass.localize("ui.components.media-browser.media_browsing_error"),text:this._renderError(e)})):this._error=e}},{kind:"method",key:"_renderError",value:function(e){return"Media directory does not exist."===e.message?o.dy`
        <h2>
          ${this.hass.localize("ui.components.media-browser.no_local_media_found")}
        </h2>
        <p>
          ${this.hass.localize("ui.components.media-browser.no_media_folder")}
          <br />
          ${this.hass.localize("ui.components.media-browser.setup_local_help","documentation",o.dy`<a
              href=${(0,_.R)(this.hass,"/more-info/local-media/setup-media")}
              target="_blank"
              rel="noreferrer"
              >${this.hass.localize("ui.components.media-browser.documentation")}</a
            >`)}
          <br />
          ${this.hass.localize("ui.components.media-browser.local_media_files")}
        </p>
      `:o.dy`<span class="error">${e.message}</span>`}},{kind:"method",key:"_setHeaderHeight",value:async function(){await this.updateComplete;const e=this._header,t=this._content;e&&t&&(this._headerOffsetHeight=e.offsetHeight,t.style.marginTop=`${this._headerOffsetHeight}px`,t.style.maxHeight=`calc(var(--media-browser-max-height, 100%) - ${this._headerOffsetHeight}px)`)}},{kind:"method",key:"_animateHeaderHeight",value:function(){let e;const t=i=>{void 0===e&&(e=i);const r=i-e;this._setHeaderHeight(),r<400&&requestAnimationFrame(t)};requestAnimationFrame(t)}},{kind:"method",decorators:[(0,a.hO)({passive:!0})],key:"_scroll",value:function(e){const t=e.currentTarget;!this._scrolled&&t.scrollTop>this._headerOffsetHeight?this._scrolled=!0:this._scrolled&&t.scrollTop<this._headerOffsetHeight&&(this._scrolled=!1)}},{kind:"get",static:!0,key:"styles",value:function(){return[w.Qx,o.iv`
        :host {
          display: flex;
          flex-direction: column;
          position: relative;
        }

        ha-circular-progress {
          --mdc-theme-primary: var(--primary-color);
          display: flex;
          justify-content: center;
          margin: 40px;
        }

        .container {
          padding: 16px;
        }

        .no-items {
          padding-left: 32px;
        }

        .highlight-add-button {
          display: flex;
          flex-direction: row-reverse;
          margin-right: 48px;
        }

        .highlight-add-button ha-svg-icon {
          position: relative;
          top: -0.5em;
          margin-left: 8px;
        }

        .content {
          overflow-y: auto;
          box-sizing: border-box;
          height: 100%;
        }

        /* HEADER */

        .header {
          display: flex;
          justify-content: space-between;
          border-bottom: 1px solid var(--divider-color);
          background-color: var(--card-background-color);
          position: absolute;
          top: 0;
          right: 0;
          left: 0;
          z-index: 5;
          padding: 16px;
        }
        .header_button {
          position: relative;
          right: -8px;
        }
        .header-content {
          display: flex;
          flex-wrap: wrap;
          flex-grow: 1;
          align-items: flex-start;
        }
        .header-content .img {
          height: 175px;
          width: 175px;
          margin-right: 16px;
          background-size: cover;
          border-radius: 2px;
          transition: width 0.4s, height 0.4s;
        }
        .header-info {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-self: stretch;
          min-width: 0;
          flex: 1;
        }
        .header-info mwc-button {
          display: block;
          --mdc-theme-primary: var(--primary-color);
          padding-bottom: 16px;
        }
        .breadcrumb {
          display: flex;
          flex-direction: column;
          overflow: hidden;
          flex-grow: 1;
          padding-top: 16px;
        }
        .breadcrumb .title {
          font-size: 32px;
          line-height: 1.2;
          font-weight: bold;
          margin: 0;
          overflow: hidden;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          padding-right: 8px;
        }
        .breadcrumb .previous-title {
          font-size: 14px;
          padding-bottom: 8px;
          color: var(--secondary-text-color);
          overflow: hidden;
          text-overflow: ellipsis;
          cursor: pointer;
          --mdc-icon-size: 14px;
        }
        .breadcrumb .subtitle {
          font-size: 16px;
          overflow: hidden;
          text-overflow: ellipsis;
          margin-bottom: 0;
          transition: height 0.5s, margin 0.5s;
        }

        .not-shown {
          font-style: italic;
          color: var(--secondary-text-color);
          padding: 8px 16px 8px;
        }

        .grid.not-shown {
          display: flex;
          align-items: center;
          text-align: center;
        }

        /* ============= CHILDREN ============= */

        mwc-list {
          --mdc-list-vertical-padding: 0;
          --mdc-list-item-graphic-margin: 0;
          --mdc-theme-text-icon-on-background: var(--secondary-text-color);
          margin-top: 10px;
        }

        mwc-list li:last-child {
          display: none;
        }

        mwc-list li[divider] {
          border-bottom-color: var(--divider-color);
        }

        mwc-list-item {
          width: 100%;
        }

        div.children {
          display: grid;
          grid-template-columns: repeat(
            auto-fit,
            minmax(var(--media-browse-item-size, 175px), 0.1fr)
          );
          grid-gap: 16px;
          padding: 16px;
        }

        :host([dialog]) .children {
          grid-template-columns: repeat(
            auto-fit,
            minmax(var(--media-browse-item-size, 175px), 0.33fr)
          );
        }

        .child {
          display: flex;
          flex-direction: column;
          cursor: pointer;
        }

        ha-card {
          position: relative;
          width: 100%;
          box-sizing: border-box;
        }

        .children ha-card .thumbnail {
          width: 100%;
          position: relative;
          box-sizing: border-box;
          transition: padding-bottom 0.1s ease-out;
          padding-bottom: 100%;
        }

        .portrait ha-card .thumbnail {
          padding-bottom: 150%;
        }

        ha-card .image {
          border-radius: 3px 3px 0 0;
        }

        .image {
          position: absolute;
          top: 0;
          right: 0;
          left: 0;
          bottom: 0;
          background-size: cover;
          background-repeat: no-repeat;
          background-position: center;
        }

        .centered-image {
          margin: 0 8px;
          background-size: contain;
        }

        .brand-image {
          background-size: 40%;
        }

        .children ha-card .icon-holder {
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .child .folder {
          color: var(--secondary-text-color);
          --mdc-icon-size: calc(var(--media-browse-item-size, 175px) * 0.4);
        }

        .child .play {
          position: absolute;
          transition: color 0.5s;
          border-radius: 50%;
          top: calc(50% - 50px);
          right: calc(50% - 35px);
          opacity: 0;
          transition: opacity 0.1s ease-out;
        }

        .child .play:not(.can_expand) {
          --mdc-icon-button-size: 70px;
          --mdc-icon-size: 48px;
        }

        ha-card:hover .play {
          opacity: 1;
        }

        ha-card:hover .play:not(.can_expand) {
          color: var(--primary-color);
        }

        ha-card:hover .play.can_expand {
          bottom: 8px;
        }

        .child .play.can_expand {
          background-color: rgba(var(--rgb-card-background-color), 0.5);
          top: auto;
          bottom: 0px;
          right: 8px;
          transition: bottom 0.1s ease-out, opacity 0.1s ease-out;
        }

        .child .play:hover {
          color: var(--primary-color);
        }

        .child .title {
          font-size: 16px;
          padding-top: 16px;
          padding-left: 2px;
          overflow: hidden;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 1;
          text-overflow: ellipsis;
        }

        .child ha-card .title {
          margin-bottom: 16px;
          padding-left: 16px;
        }

        mwc-list-item .graphic {
          background-size: contain;
          border-radius: 2px;
          display: flex;
          align-content: center;
          align-items: center;
          line-height: initial;
        }

        mwc-list-item .graphic .play {
          opacity: 0;
          transition: all 0.5s;
          background-color: rgba(var(--rgb-card-background-color), 0.5);
          border-radius: 50%;
          --mdc-icon-button-size: 40px;
        }

        mwc-list-item:hover .graphic .play {
          opacity: 1;
          color: var(--primary-text-color);
        }

        mwc-list-item .graphic .play.show {
          opacity: 1;
          background-color: transparent;
        }

        mwc-list-item .title {
          margin-left: 16px;
        }
        mwc-list-item[dir="rtl"] .title {
          margin-right: 16px;
          margin-left: 0;
        }

        /* ============= Narrow ============= */

        :host([narrow]) {
          padding: 0;
        }

        :host([narrow]) .media-source {
          padding: 0 24px;
        }

        :host([narrow]) div.children {
          grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) !important;
        }

        :host([narrow]) .breadcrumb .title {
          font-size: 24px;
        }
        :host([narrow]) .header {
          padding: 0;
        }
        :host([narrow]) .header.no-dialog {
          display: block;
        }
        :host([narrow]) .header_button {
          position: absolute;
          top: 14px;
          right: 8px;
        }
        :host([narrow]) .header-content {
          flex-direction: column;
          flex-wrap: nowrap;
        }
        :host([narrow]) .header-content .img {
          height: auto;
          width: 100%;
          margin-right: 0;
          padding-bottom: 50%;
          margin-bottom: 8px;
          position: relative;
          background-position: center;
          border-radius: 0;
          transition: width 0.4s, height 0.4s, padding-bottom 0.4s;
        }
        ha-fab {
          position: absolute;
          --mdc-theme-secondary: var(--primary-color);
          bottom: -20px;
          right: 20px;
        }
        :host([narrow]) .header-info mwc-button {
          margin-top: 16px;
          margin-bottom: 8px;
        }
        :host([narrow]) .header-info {
          padding: 0 16px 8px;
        }

        /* ============= Scroll ============= */
        :host([scroll]) .breadcrumb .subtitle {
          height: 0;
          margin: 0;
        }
        :host([scroll]) .breadcrumb .title {
          -webkit-line-clamp: 1;
        }
        :host(:not([narrow])[scroll]) .header:not(.no-img) ha-icon-button {
          align-self: center;
        }
        :host([scroll]) .header-info mwc-button,
        .no-img .header-info mwc-button {
          padding-right: 4px;
        }
        :host([scroll][narrow]) .no-img .header-info mwc-button {
          padding-right: 16px;
        }
        :host([scroll]) .header-info {
          flex-direction: row;
        }
        :host([scroll]) .header-info mwc-button {
          align-self: center;
          margin-top: 0;
          margin-bottom: 0;
          padding-bottom: 0;
        }
        :host([scroll][narrow]) .no-img .header-info {
          flex-direction: row-reverse;
        }
        :host([scroll][narrow]) .header-info {
          padding: 20px 24px 10px 24px;
          align-items: center;
        }
        :host([scroll]) .header-content {
          align-items: flex-end;
          flex-direction: row;
        }
        :host([scroll]) .header-content .img {
          height: 75px;
          width: 75px;
        }
        :host([scroll]) .breadcrumb {
          padding-top: 0;
          align-self: center;
        }
        :host([scroll][narrow]) .header-content .img {
          height: 100px;
          width: 100px;
          padding-bottom: initial;
          margin-bottom: 0;
        }
        :host([scroll]) ha-fab {
          bottom: 0px;
          right: -24px;
          --mdc-fab-box-shadow: none;
          --mdc-theme-secondary: rgba(var(--rgb-primary-color), 0.5);
        }

        lit-virtualizer {
          height: 100%;
          overflow: overlay !important;
          contain: size layout !important;
        }

        lit-virtualizer.not_shown {
          height: calc(100% - 36px);
        }
      `]}}]}}),o.oi)},23469:(e,t,i)=>{i.d(t,{Qr:()=>a,aV:()=>n,b:()=>r,oE:()=>o});const r=(e,t)=>e.callWS({type:"media_source/browse_media",media_content_id:t}),n=e=>e.startsWith("media-source://media_source"),o=async(e,t,i)=>{const r=new FormData;r.append("media_content_id",t),r.append("file",i);const n=await e.fetchWithAuth("/api/media_source/local_source/upload",{method:"POST",body:r});if(413===n.status)throw new Error(`Uploaded file is too large (${i.name})`);if(200!==n.status)throw new Error("Unknown error");return n.json()},a=async(e,t)=>e.callWS({type:"media_source/local_source/remove",media_content_id:t})}}]);