"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[26136],{26136:(t,a,r)=>{r.a(t,(async(t,s)=>{try{r.r(a);var e=r(37500),i=r(50467),c=r(99476),n=t([c]);c=(n.then?(await n)():n)[0];class o extends c.p{async getCardSize(){if(!this._cards)return 0;const t=[];for(const a of this._cards)t.push((0,i.N)(a));return(await Promise.all(t)).reduce(((t,a)=>t+a),0)}static get styles(){return[super.sharedStyles,e.iv`
        #root {
          display: flex;
          flex-direction: column;
          height: 100%;
        }
        #root > * {
          margin: var(
            --vertical-stack-card-margin,
            var(--stack-card-margin, 4px 0)
          );
        }
        #root > *:first-child {
          margin-top: 0;
        }
        #root > *:last-child {
          margin-bottom: 0;
        }
      `]}}customElements.define("hui-vertical-stack-card",o),s()}catch(t){s(t)}}))}}]);
//# sourceMappingURL=35a90ab0.js.map