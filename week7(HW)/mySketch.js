//Forked from https://www.openprocessing.org/sketch/1038378
//Original idea from https://twitter.com/takawo/status/1336676902900170757
let blocks = [];
let videoInput;
let faceTracker;
let tmp;
let platform;
let canvas;
let counter = 0;
let wallOff = false;

let myString = "";
let myWords = [];
let wordIndex = 0;
let input;


function setup() {
  canvas = createCanvas(640, 480);
  //colorMode(HSB, 360, 100, 100, 100);
  pixelDensity(1);
  textSize(32);

  input = createInput("I am not interested in you");
  input.position(10, 15);
  input.input(onInput); 

  let constraints = {
    video: {
      mandatory: {
        minWidth: 640,
        minHeight: 480
      },
      optional: [{
        maxFrameRate: 200
      }]
    },
    audio: false
  };

  videoInput = createCapture(constraints);
  videoInput.size(640, 480);
  videoInput.hide();

  faceTracker = new clm.tracker();
  faceTracker.init();
  faceTracker.start(videoInput.elt);

  matter.init();
  platform = matter.makeBarrier(width / 2, height, width, 1);
}

function draw() {
  myWords = trim(input.value()).split(" ");

  tmp = videoInput.get();

  let scl = height / tmp.height;
  let margin = (tmp.width * scl - width) / 2
  push();
  translate(-margin, 0);
  image(tmp, 0, 0, tmp.width * scl, tmp.height * scl);
  fill(255);
  noStroke();
  // platform.show();
  let positions = faceTracker.getCurrentPosition();
  // faceTracker.draw(canvas.elt);
  if (positions !== false && frameCount % 10 == 0) {
    let wx = abs(positions[13][0] - positions[1][0]) * 1.1;
    let wy = abs(positions[7][1] - min(positions[16][1], positions[20][1])) * 1.1;
    let x = positions[62][0] - wx / 2;
    let y = positions[62][1] - wy / 2;
    let face = tmp.get(x, y, wx, wy);
    let mouthTop = createVector(positions[60][0], positions[60][1]);
    let mouthBottom = createVector(positions[57][0], positions[57][1]);
    let mouthLeft = createVector(positions[44][0], positions[44][1]);
    let mouthRight = createVector(positions[50][0], positions[50][1]);
    let mouthHeight = p5.Vector.dist(mouthTop, mouthBottom);
    let mouthWidth = p5.Vector.dist(mouthLeft, mouthRight);
    let mouseCenter = p5.Vector.lerp(mouthTop, mouthBottom, 0.5);
    let mw = mouthWidth * scl;
    let mh = mouthHeight * scl;
    let mx = mouseCenter.x * scl + mw / 2;
    let my = mouseCenter.y * scl + mh / 2;
    let face_scl = mw / wx;

    if (mw > 15 && mh > 15) {
      
      let s = myWords[wordIndex];
      let sWidth = textWidth(s);
      let sHeight = 32;

      makeFaceBlock(mx / scl - mw / scl / 2, my / scl - mh / scl / 2, sWidth, sHeight, face, s);
      wordIndex++;
  if (wordIndex > myWords.length-1) wordIndex = 0;
    }
  }

  for (let i = blocks.length - 1; i >= 0; i--) {
    let b = blocks[i];
    b.show();
    let p = b.body.position;
    push();
    translate(p.x, p.y, 0);
    rotate(b.body.angle);
    imageMode(CENTER);
    //if (typeof b.img === "undefined") return;
    //image(b.img, 0, 0, b.width, b.height);
    textAlign(CENTER, CENTER);
    fill(0,40,105);
    text(b.str, 0, 0);
    // rectMode(CENTER);
    // rect(0,0,b.width*1.1,b.height*1.1)
    pop();
    if (b.isOffCanvas()) {
      matter.forget(b);
      blocks.splice(i, 1);
    }
  }
  pop();


  fill(255, 0,0)

  if (blocks.length == 25) {
    matter.forget(platform);
    wallOff = true;
  }
  if (blocks.length == 0 && wallOff) {
    platform = matter.makeBarrier(width / 2, height, width, 1);
    wallOff = false;
  }

}

function makeFaceBlock(cx, cy, w, h, img, myString) {
  let scl = 1;
  let dw = w * scl;
  let dh = h * scl;
  let b = matter.makeBlock(cx, cy, dw, dh);
  let face = tmp.get(cx, cy, w, h);
  face.resize(face.width * scl, face.height * scl);
  b.img = img;
  b.str = myString;
  // let angle = random(TWO_PI);
  // b.setAngle(angle)
  blocks.push(b);
}

function onInput() {
  wordIndex = 0;
}
