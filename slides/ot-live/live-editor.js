(() => {
  const slides=[...document.querySelectorAll('body>svg[data-marpit-svg]')];
  let active=0;
  function show(i){active=Math.max(0,Math.min(slides.length-1,i));slides.forEach((s,n)=>s.style.display=n===active?'block':'none');document.querySelector('#ot-page').textContent=(active+1)+' / '+slides.length;document.querySelector('#ot-prev').disabled=active===0;document.querySelector('#ot-next').disabled=active===slides.length-1;}
  document.querySelector('#ot-prev').onclick=()=>{document.activeElement.blur();show(active-1);};
  document.querySelector('#ot-next').onclick=()=>{document.activeElement.blur();show(active+1);};
  document.addEventListener('keydown',e=>{if(e.isComposing||e.target.closest('input,button,a'))return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();show(active+1);}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();show(active-1);}if(e.key==='Home'){e.preventDefault();show(0);}if(e.key==='End'){e.preventDefault();show(slides.length-1);}});
  show(0);
})();
