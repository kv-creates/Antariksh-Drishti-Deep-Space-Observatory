// Antariksh-Drishti dashboard interactivity — zero dependencies
(function(){
  "use strict";
  const $=id=>document.getElementById(id);
  // mission clock
  const t0=Date.now(); const clock=$("clock");
  setInterval(()=>{ if(!clock) return; const s=Math.floor((Date.now()-t0)/1000);
    const h=String(Math.floor(s/3600)).padStart(2,"0"),m=String(Math.floor(s%3600/60)).padStart(2,"0"),ss=String(s%60).padStart(2,"0");
    clock.textContent="T+ "+h+":"+m+":"+ss; },1000);
  // orbit period: T=2pi sqrt(a^3/mu)
  const MU=398600.4418, alt=$("alt"), altV=$("alt-val"), perV=$("period-val"), perM=$("period-min"), oc=$("orbit-canvas");
  function period(a){return 2*Math.PI*Math.sqrt(Math.pow(a,3)/MU);}
  function drawOrbit(a){ if(!oc) return; const c=oc.getContext("2d"); const W=oc.width,H=oc.height;
    c.clearRect(0,0,W,H); c.fillStyle="#070c18"; c.fillRect(0,0,W,H);
    // stars
    c.fillStyle="rgba(255,255,255,.7)"; for(let i=0;i<70;i++){c.fillRect((i*73)%W,(i*37)%H,1.4,1.4);}
    const cx=W/2,cy=H/2, r1=52, r2=52+(a-6600)/(42000-6600)*70;
    c.strokeStyle="#60a5fa"; c.lineWidth=2.5; c.beginPath(); c.ellipse(cx,cy,r1,r1*.62,0,0,7); c.stroke();
    c.strokeStyle="#34d399"; c.setLineDash([6,4]); c.beginPath(); c.ellipse(cx,cy,r2,r2*.62,0,0,7); c.stroke(); c.setLineDash([]);
    c.fillStyle="#facc15"; c.beginPath(); c.arc(cx,cy,9,0,7); c.fill();
    c.fillStyle="#e2e8f0"; c.font="12px system-ui"; c.fillText("a="+Math.round(a)+" km",12,H-12);
  }
  function updAlt(){ if(!alt) return; const a=+alt.value; const T=period(a);
    altV.textContent=a+" km"; perV.textContent=Math.round(T)+" s"; perM.textContent=(T/60).toFixed(1)+" min"; drawOrbit(a); }
  const inc=document.getElementById("inc");
  function drawOrbitTilt(a, incDeg){ if(!oc) return; drawOrbit(a); const c=oc.getContext("2d"); c.fillStyle="#94a3b8"; c.font="11px system-ui"; c.fillText("i="+incDeg+" deg", 12, 22); }
  function updAll(){ const a=+alt.value, i=inc?+inc.value:51; const T=period(a); altV.textContent=a+" km"; perV.textContent=Math.round(T)+" s"; perM.textContent=(T/60).toFixed(1)+" min"; drawOrbitTilt(a,i); }
  if(alt){alt.addEventListener("input",updAll); if(inc) inc.addEventListener("input",updAll); updAll(); }
  // lightcurve sketch + threshold
  const th=$("thresh"), out=$("detect-out"), lc=$("lc-canvas");
  function drawLC(){ if(!lc) return; const c=lc.getContext("2d"); const W=lc.width,H=lc.height;
    c.clearRect(0,0,W,H); c.fillStyle="#f8fafc"; c.fillRect(0,0,W,H);
    c.strokeStyle="#0b3d91"; c.lineWidth=2; c.beginPath();
    for(let x=0;x<=W;x++){ const day=x/W*10; const f=(day>4.9&&day<5.1)?0.988:1; const y=20+(1-f)*3000+ (1-1)*10 + (1-f===0?18:0);
      const yy=f===1?40:110; x===0?c.moveTo(x,yy):c.lineTo(x,yy); }
    c.stroke(); c.fillStyle="#64748b"; c.font="11px system-ui"; c.fillText("days 0 → 10",10,H-8); c.fillText("flux",8,14);
  }
  const tv=document.getElementById("thresh-val");
  function updTh(){ if(!th) return; const t=+th.value; if(tv) tv.textContent=t.toFixed(1)+"%"; const detected=1.2>t; out.textContent=detected?"CANDIDATE ✓":"NULL ✗"; out.style.color=detected?"#059669":"#dc2626"; drawLC(); }
  if(th){th.addEventListener("input",updTh); updTh();}
  // SNR calc: F/sqrt(F+B+RN^2)
  const fl=$("flux"), bg=$("bg"), sv=$("snr-val"), sc=$("snr-canvas");
  function updSNR(){ if(!fl) return; const F=+fl.value,B=+bg.value,RN=5; const snr=F/Math.sqrt(F+B+RN*RN);
    sv.textContent=snr.toFixed(1)+" σ"; if(!sc) return; const c=sc.getContext("2d"); c.clearRect(0,0,sc.width,sc.height);
    c.fillStyle="#0b142b"; c.fillRect(0,0,sc.width,sc.height);
    const w=Math.min(1,snr/80)*sc.width; const g=c.createLinearGradient(0,0,sc.width,0); g.addColorStop(0,"#2563eb"); g.addColorStop(1,"#34d399");
    c.fillStyle=g; c.fillRect(0,40,w,44); c.fillStyle="#94a3b8"; c.font="12px system-ui"; c.fillText("0",4,120); c.fillText("80σ",sc.width-36,120);
  }
  if(fl){fl.addEventListener("input",updSNR); bg.addEventListener("input",updSNR); updSNR();}
  // smooth anchor offset handled by CSS scroll-margin
})();

// theme toggle
const btn=document.getElementById("theme-btn"), root=document.documentElement;
const saved=localStorage.getItem("ad-theme"); if(saved) root.setAttribute("data-theme",saved);
if(btn) btn.addEventListener("click",()=>{ const cur=root.getAttribute("data-theme")==="light"?"dark":"light"; root.setAttribute("data-theme",cur); localStorage.setItem("ad-theme",cur); });

document.querySelectorAll(".chip").forEach(b=>b.addEventListener("click",()=>{
  document.querySelectorAll(".chip").forEach(x=>x.classList.remove("active")); b.classList.add("active");
  const f=b.dataset.f; document.querySelectorAll(".queue li").forEach(li=>{
    const txt=li.textContent; const show = f==="all" || (f==="high" && txt.includes("pri 9")) || (f==="saa" && !txt.includes("SAA"));
    li.style.display=show?"flex":"none";
  });
}));
