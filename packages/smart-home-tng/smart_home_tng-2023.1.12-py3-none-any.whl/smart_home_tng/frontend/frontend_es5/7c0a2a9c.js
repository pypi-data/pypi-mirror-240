"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[89173],{89173:function(t,s,a){a.r(s);var r=a(37500),e=a(50467),i=a(99476);class n extends i.p{async getCardSize(){if(!this._cards)return 0;const t=[];for(const a of this._cards)t.push((0,e.N)(a));const s=await Promise.all(t);return Math.max(...s)}static get styles(){return[super.sharedStyles,r.iv`
        #root {
          display: flex;
          height: 100%;
        }
        #root > * {
          flex: 1 1 0;
          margin: var(
            --horizontal-stack-card-margin,
            var(--stack-card-margin, 0 4px)
          );
          min-width: 0;
        }
        #root > *:first-child {
          margin-left: 0;
        }
        #root > *:last-child {
          margin-right: 0;
        }
      `]}}customElements.define("hui-horizontal-stack-card",n)}}]);
//# sourceMappingURL=7c0a2a9c.js.map