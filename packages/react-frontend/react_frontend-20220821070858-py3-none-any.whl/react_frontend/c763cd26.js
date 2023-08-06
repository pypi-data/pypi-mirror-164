"use strict";(self.webpackChunkreact_frontend=self.webpackChunkreact_frontend||[]).push([[7222],{7222:(e,i,t)=>{t.r(i),t.d(i,{DialogAddApplicationCredential:()=>k});t(55398),t(47512);var r=t(17871),n=t(26445),a=t(18394),o=(t(84224),t(16591),t(9828));t(75504),t(51520);var s=t(64346),l=t(29950);function d(){d=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,i){["method","field"].forEach((function(t){i.forEach((function(i){i.kind===t&&"own"===i.placement&&this.defineClassElement(e,i)}),this)}),this)},initializeClassElements:function(e,i){var t=e.prototype;["method","field"].forEach((function(r){i.forEach((function(i){var n=i.placement;if(i.kind===r&&("static"===n||"prototype"===n)){var a="static"===n?e:t;this.defineClassElement(a,i)}}),this)}),this)},defineClassElement:function(e,i){var t=i.descriptor;if("field"===i.kind){var r=i.initializer;t={enumerable:t.enumerable,writable:t.writable,configurable:t.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,i.key,t)},decorateClass:function(e,i){var t=[],r=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!p(e))return t.push(e);var i=this.decorateElement(e,n);t.push(i.element),t.push.apply(t,i.extras),r.push.apply(r,i.finishers)}),this),!i)return{elements:t,finishers:r};var a=this.decorateConstructor(t,i);return r.push.apply(r,a.finishers),a.finishers=r,a},addElementPlacement:function(e,i,t){var r=i[e.placement];if(!t&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,i){for(var t=[],r=[],n=e.decorators,a=n.length-1;a>=0;a--){var o=i[e.placement];o.splice(o.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[a])(s)||s);e=l.element,this.addElementPlacement(e,i),l.finisher&&r.push(l.finisher);var d=l.extras;if(d){for(var c=0;c<d.length;c++)this.addElementPlacement(d[c],i);t.push.apply(t,d)}}return{element:e,finishers:r,extras:t}},decorateConstructor:function(e,i){for(var t=[],r=i.length-1;r>=0;r--){var n=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,i[r])(n)||n);if(void 0!==a.finisher&&t.push(a.finisher),void 0!==a.elements){e=a.elements;for(var o=0;o<e.length-1;o++)for(var s=o+1;s<e.length;s++)if(e[o].key===e[s].key&&e[o].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[o].key+")")}}return{elements:e,finishers:t}},fromElementDescriptor:function(e){var i={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(i,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(i.initializer=e.initializer),i},toElementDescriptors:function(e){var i;if(void 0!==e)return(i=e,function(e){if(Array.isArray(e))return e}(i)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(i)||function(e,i){if(e){if("string"==typeof e)return v(e,i);var t=Object.prototype.toString.call(e).slice(8,-1);return"Object"===t&&e.constructor&&(t=e.constructor.name),"Map"===t||"Set"===t?Array.from(e):"Arguments"===t||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t)?v(e,i):void 0}}(i)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var i=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),i}),this)},toElementDescriptor:function(e){var i=String(e.kind);if("method"!==i&&"field"!==i)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+i+'"');var t=m(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:i,key:t,placement:r,descriptor:Object.assign({},n)};return"field"!==i?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:f(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var i={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(i,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),i},toClassDescriptor:function(e){var i=String(e.kind);if("class"!==i)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+i+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var t=f(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:t}},runClassFinishers:function(e,i){for(var t=0;t<i.length;t++){var r=(0,i[t])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,i,t){if(void 0!==e[i])throw new TypeError(t+" can't have a ."+i+" property.")}};return e}function c(e){var i,t=m(e.key);"method"===e.kind?i={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?i={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?i={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(i={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:t,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:i};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function h(e,i){void 0!==e.descriptor.get?i.descriptor.get=e.descriptor.get:i.descriptor.set=e.descriptor.set}function p(e){return e.decorators&&e.decorators.length}function u(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function f(e,i){var t=e[i];if(void 0!==t&&"function"!=typeof t)throw new TypeError("Expected '"+i+"' to be a function");return t}function m(e){var i=function(e,i){if("object"!=typeof e||null===e)return e;var t=e[Symbol.toPrimitive];if(void 0!==t){var r=t.call(e,i||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===i?String:Number)(e)}(e,"string");return"symbol"==typeof i?i:String(i)}function v(e,i){(null==i||i>e.length)&&(i=e.length);for(var t=0,r=new Array(i);t<i;t++)r[t]=e[t];return r}const y=e=>r.dy`<mwc-list-item>
  <span>${e.name}</span>
</mwc-list-item>`;let k=function(e,i,t,r){var n=d();if(r)for(var a=0;a<r.length;a++)n=r[a](n);var o=i((function(e){n.initializeInstanceElements(e,s.elements)}),t),s=n.decorateClass(function(e){for(var i=[],t=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},r=0;r<e.length;r++){var n,a=e[r];if("method"===a.kind&&(n=i.find(t)))if(u(a.descriptor)||u(n.descriptor)){if(p(a)||p(n))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");n.descriptor=a.descriptor}else{if(p(a)){if(p(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");n.decorators=a.decorators}h(a,n)}else i.push(a)}return i}(o.d.map(c)),e);return n.initializeClassElements(o.F,s.elements),n.runClassFinishers(o.F,s.finishers)}([(0,n.Mo)("dialog-add-application-credential")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_loading",value:()=>!1},{kind:"field",decorators:[(0,n.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_domain",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_name",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_description",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_clientId",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_clientSecret",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_domains",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_config",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._domain=void 0!==e.selectedDomain?e.selectedDomain:"",this._name="",this._description="",this._clientId="",this._clientSecret="",this._error=void 0,this._loading=!1,this._fetchConfig()}},{kind:"method",key:"_fetchConfig",value:async function(){this._config=await(async e=>e.callWS({type:"application_credentials/config"}))(this.hass),this._domains=Object.keys(this._config.integrations).map((e=>({id:e,name:(0,s.Lh)(this.hass.localize,e)}))),await this.hass.loadBackendTranslation("application_credentials"),""!==this._domain&&this._updateDescription()}},{kind:"method",key:"render",value:function(){return this._params&&this._domains?r.dy`
      <ha-dialog
        open
        @closed=${this._abortDialog}
        scrimClickAction
        escapeKeyAction
        .heading=${(0,o.i)(this.hass,this.hass.localize("ui.panel.config.application_credentials.editor.caption"))}
      >
        <div>
          ${this._error?r.dy` <div class="error">${this._error}</div> `:""}
          <ha-combo-box
            name="domain"
            .hass=${this.hass}
            .disabled=${!!this._params.selectedDomain}
            .label=${this.hass.localize("ui.panel.config.application_credentials.editor.domain")}
            .value=${this._domain}
            .renderer=${y}
            .items=${this._domains}
            item-id-path="id"
            item-value-path="id"
            item-label-path="name"
            required
            @value-changed=${this._handleDomainPicked}
          ></ha-combo-box>
          ${this._description?r.dy`<ha-markdown
                breaks
                .content=${this._description}
              ></ha-markdown>`:""}
          <ha-textfield
            class="name"
            name="name"
            .label=${this.hass.localize("ui.panel.config.application_credentials.editor.name")}
            .value=${this._name}
            required
            @input=${this._handleValueChanged}
            error-message=${this.hass.localize("ui.common.error_required")}
            dialogInitialFocus
          ></ha-textfield>
          <ha-textfield
            class="clientId"
            name="clientId"
            .label=${this.hass.localize("ui.panel.config.application_credentials.editor.client_id")}
            .value=${this._clientId}
            required
            @input=${this._handleValueChanged}
            error-message=${this.hass.localize("ui.common.error_required")}
            dialogInitialFocus
          ></ha-textfield>
          <ha-textfield
            .label=${this.hass.localize("ui.panel.config.application_credentials.editor.client_secret")}
            type="password"
            name="clientSecret"
            .value=${this._clientSecret}
            required
            @input=${this._handleValueChanged}
            error-message=${this.hass.localize("ui.common.error_required")}
          ></ha-textfield>
        </div>
        ${this._loading?r.dy`
              <div slot="primaryAction" class="submit-spinner">
                <ha-circular-progress active></ha-circular-progress>
              </div>
            `:r.dy`
              <mwc-button
                slot="primaryAction"
                .disabled=${!this._domain||!this._clientId||!this._clientSecret}
                @click=${this._createApplicationCredential}
              >
                ${this.hass.localize("ui.panel.config.application_credentials.editor.create")}
              </mwc-button>
            `}
      </ha-dialog>
    `:r.dy``}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,this._domains=void 0,(0,a.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"_handleDomainPicked",value:function(e){e.stopPropagation(),this._domain=e.detail.value,this._updateDescription()}},{kind:"method",key:"_updateDescription",value:function(){const e=this._config.integrations[this._domain];this._description=this.hass.localize(`component.${this._domain}.application_credentials.description`,e.description_placeholders)}},{kind:"method",key:"_handleValueChanged",value:function(e){this._error=void 0;const i=e.target.name,t=e.target.value;this[`_${i}`]=t}},{kind:"method",key:"_abortDialog",value:function(){this._params&&this._params.dialogAbortedCallback&&this._params.dialogAbortedCallback(),this.closeDialog()}},{kind:"method",key:"_createApplicationCredential",value:async function(e){if(e.preventDefault(),!this._domain||!this._clientId||!this._clientSecret)return;let i;this._loading=!0,this._error="";try{i=await(async(e,i,t,r,n)=>e.callWS({type:"application_credentials/create",domain:i,client_id:t,client_secret:r,name:n}))(this.hass,this._domain,this._clientId,this._clientSecret,this._name)}catch(e){return this._loading=!1,void(this._error=e.message)}this._params.applicationCredentialAddedCallback(i),this.closeDialog()}},{kind:"get",static:!0,key:"styles",value:function(){return[l.yu,r.iv`
        ha-dialog {
          --mdc-dialog-max-width: 500px;
          --dialog-z-index: 10;
        }
        .row {
          display: flex;
          padding: 8px 0;
        }
        ha-combo-box {
          display: block;
          margin-bottom: 24px;
        }
        ha-textfield {
          display: block;
          margin-bottom: 24px;
        }
      `]}}]}}),r.oi)}}]);