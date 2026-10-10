(() => {
  const slides=[...document.querySelectorAll('body>svg[data-marpit-svg]')];
  let active=0, editing=true, composing=false;
  function editable(){document.querySelectorAll('section h1,section h2,section h3,section marp-h1,section marp-h2,section p,section li,section td,section th,.ot-options span').forEach(el=>{if(el.querySelector('li,p,input,a,img'))return;el.contentEditable=editing?'plaintext-only':'false';el.spellcheck=false;});}
  function show(i){active=Math.max(0,Math.min(slides.length-1,i));slides.forEach((s,n)=>s.style.display=n===active?'block':'none');document.querySelector('#ot-page').textContent=(active+1)+' / '+slides.length;document.querySelector('#ot-prev').disabled=active===0;document.querySelector('#ot-next').disabled=active===slides.length-1;}
  document.querySelector('#ot-prev').onclick=()=>{document.activeElement.blur();show(active-1);};
  document.querySelector('#ot-next').onclick=()=>{document.activeElement.blur();show(active+1);};
  document.querySelector('#ot-edit').onclick=()=>{editing=!editing;editable();document.querySelector('#ot-edit').textContent=editing?'발표 모드':'편집 모드';document.querySelectorAll('section input').forEach(c=>c.disabled=!editing);document.querySelectorAll('[data-add-row]').forEach(c=>c.hidden=!editing);};
  document.addEventListener('compositionstart',()=>composing=true);document.addEventListener('compositionend',()=>composing=false);
  document.addEventListener('keydown',e=>{if(composing||e.isComposing||e.keyCode===229||e.target.closest('[contenteditable="plaintext-only"],input,button,a'))return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();show(active+1);}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();show(active-1);}if(e.key==='Home'){e.preventDefault();show(0);}if(e.key==='End'){e.preventDefault();show(slides.length-1);}});
  document.addEventListener('click',e=>{const btn=e.target.closest('[data-add-row]');if(!btn)return;const t=[...document.querySelectorAll('table[data-add-rows]')].find(t=>t.dataset.addRows===btn.dataset.addRow);const row=t.tBodies[0].insertRow();for(let i=0;i<t.tHead.rows[0].cells.length;i++)row.insertCell().textContent='';editable();row.cells[0].focus();});
  editable();show(0);
})();
