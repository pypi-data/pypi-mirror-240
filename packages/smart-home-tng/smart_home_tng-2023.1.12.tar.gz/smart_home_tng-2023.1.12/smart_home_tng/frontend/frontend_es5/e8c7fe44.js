"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[26136],{26136:function(t,r,s){s.r(r);var a=s(37500),e=s(50467),i=s(99476);class n extends i.p{async getCardSize(){if(!this._cards)return 0;const t=[];for(const r of this._cards)t.push((0,e.N)(r));return(await Promise.all(t)).reduce(((t,r)=>t+r),0)}static get styles(){return[super.sharedStyles,a.iv`
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
      `]}}customElements.define("hui-vertical-stack-card",n)}}]);
//# sourceMappingURL=e8c7fe44.js.map