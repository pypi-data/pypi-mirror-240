"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[89173],{89173:(t,a,s)=>{s.a(t,(async(t,r)=>{try{s.r(a);var e=s(37500),i=s(50467),n=s(99476),c=t([n]);n=(c.then?(await c)():c)[0];class o extends n.p{async getCardSize(){if(!this._cards)return 0;const t=[];for(const a of this._cards)t.push((0,i.N)(a));const a=await Promise.all(t);return Math.max(...a)}static get styles(){return[super.sharedStyles,e.iv`
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
      `]}}customElements.define("hui-horizontal-stack-card",o),r()}catch(t){r(t)}}))}}]);
//# sourceMappingURL=86916c55.js.map