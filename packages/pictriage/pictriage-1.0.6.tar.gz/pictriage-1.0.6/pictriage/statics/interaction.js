let sizeInput = document.querySelector('#img_width');
let lens = document.querySelector('#lens');
let galleriesEl = document.querySelector('#galleries');


// put it inline because otherwise have to think about whether it will load before/after the images

function getClickAction() {
  let form = document.querySelector('#action-form');
  return form.elements.action.value;
}



function renderClickAction() {
  let cursor = getClickAction() === NONE_CLICK_ACTION ? null : 'pointer';
  for (let ele of document.querySelectorAll('.clickable')) {
    ele.style.cursor = cursor;
  }
}

renderClickAction();

for (let ele of document.querySelectorAll('.clickable')) {
  ele.onclick = async function () {
    if (getClickAction() === NONE_CLICK_ACTION) alert("Please select an action first");
    let btn = this;
    const settings = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: this.dataset.fp
    };
    let response = await fetch('/clicked', settings)
    if (!response.ok) {
      alert("An error occurred. Check your terminal for details.");
      return;
    }
    let imgContainer;
    if (ele.dataset.isfolder) {
      imgContainer = ele.closest('.folder');
    } else {
      imgContainer = ele;
    }
    let containerHasImage = false;
    for (let img of imgContainer.querySelectorAll('.gallery-img')) {
      // this is supposed to force reload but doesn't seem enough
      let response = await fetch(img.src, { cache: 'reload', mode: 'no-cors' })
      if (response.ok) {
        // force reload
        img.src = `${img.src}#${Date.now()}`;
        containerHasImage = true;
      } else {
        img.style.display = 'none';
      }
    }
    if (!containerHasImage) imgContainer.style.display = 'none';
  }
}


function renderLensVisibility() {
  
  let lensStyle, marginLeft;
  if (document.querySelector('[name=lens_visibility]').checked) {
      lensStyle = '';
      marginLeft = zoom_pane_width;
  } else {
      lensStyle = 'none';
      marginLeft = '0';
  }
  lens.style.display = lensStyle;
  galleriesEl.style.marginLeft = marginLeft;
}

renderLensVisibility();


function renderThumbnailSize() {
  let size = parseInt(sizeInput.value);
  if (isNaN(size)) return;
  let sizeAsPx = size + 'px';
  for (let img of document.querySelectorAll('.gallery-img')) {
    img.style.maxWidth = sizeAsPx;
    img.style.maxHeight = sizeAsPx;
  }
}

renderThumbnailSize();

sizeInput.addEventListener('change', renderThumbnailSize);
