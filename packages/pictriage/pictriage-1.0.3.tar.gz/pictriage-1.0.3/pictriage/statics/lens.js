let zoomedImg;
let thumb;
let thumbRect;
let mainContentWidth;
let lensWidth;
function setUpHover() {
  for (let img of document.querySelectorAll('.gallery-img')) {
    img.addEventListener('mouseover', function (event) {
      thumb = this;
      zoomedImg = thumb.cloneNode(true);
      // override images that might be zoomed
      zoomedImg.style.maxWidth = 'none';
      zoomedImg.style.maxHeight = 'none';
      lens.replaceChildren(zoomedImg);
      thumbRect = event.target.getBoundingClientRect();
      lensWidth = lens.offsetWidth;
    });
    img.onmousemove = function (event) {
      let img = this;

      // vertical pan
      let yFrac = (event.clientY - thumbRect.top) / thumb.height;
      let lensHeight = window.innerHeight;
      let middlePixel = zoomedImg.height * yFrac;
      let hiddenPixels = middlePixel - lensHeight / 2
      let boundedTop = Math.max(0, hiddenPixels)
      let boundedTopAndBottom = Math.min(boundedTop, zoomedImg.height - lensHeight);
      let marginTop = -Math.round(boundedTopAndBottom);
      zoomedImg.style.marginTop = `${marginTop}px`;

      // horizontal pan
      let xFrac = (event.clientX - thumbRect.left) / thumb.width;
      middlePixel = zoomedImg.width * xFrac;
      hiddenPixels = middlePixel - lensWidth / 2
      let boundedLeft = Math.max(0, hiddenPixels)
      let boundedLeftAndRight = Math.min(boundedLeft, zoomedImg.width - lensWidth);
      let marginLeft = -Math.round(boundedLeftAndRight);
      zoomedImg.style.marginLeft = `${marginLeft}px`;
    }
  }
}
if (lens) setUpHover();

