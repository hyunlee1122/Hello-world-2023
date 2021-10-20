let over, respawnTime, m;
let ball, racketss, hit;

function preload() {
  hit = loadSound("assets/hit.mp3");
  win = loadSound("assets/win.mp3");
}

function setup() {
  createCanvas(500, 400);
  textSize(100);
  textAlign(CENTER, CENTER);
  noStroke();
  restart();
}

function restart() {
  over = false;
  respawmTime = 1000;
  ball = new Ball(20)
  racketss = [new rackets(20, 12, 40, [87, 83]), new rackets(width - 20, 12, 40, [UP_ARROW, DOWN_ARROW])];
}

function reset() {
  m = millis()
  if (ball.side == 0) {
    racketss[0].score += 1;
  } else {
    racketss[1].score += 1;
  }
  ball = null;
  if (racketss[0].score > 4 || racketss[1].score > 4) {
    win.play();
    over = true;
    respawmTime = 2000;
  }
}

function draw() {
  background(500);

  if (ball) {
    ball.update();
    ball.checkCollision(racketss);
    ball.show();
    if (ball.checkGameOver()) {
      reset();
    }
  } else {
    if (millis() > m + respawmTime) {
      ball = new Ball(20);
      if (over) {
        restart();
      }
    }
  }

  for (let i = 0; i < racketss.length; i++) {
    if (!over) {
      racketss[i].update();
      racketss[i].show();
    }
  }

  for (let i = 8; i < height; i += height / 10) {
    fill(50, 20)
  }
  text(racketss[0].score, width / 4, height / 4);
  text(racketss[1].score, 3 * width / 4, height / 4);
}
