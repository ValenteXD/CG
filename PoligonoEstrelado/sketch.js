let radius = 200;
let inner_radius = 100;
let n = 3;

function setup() {
    createCanvas(1920,1000);
    frameRate(360);
}  

function draw() {
    background(255);
    translate(width/2,height/2);
    let [mx,my] = relativeMouse();
    let v = createVector(1,0);
    let u = createVector(mx,my);
    rotate(v.angleBetween(u));
    n = floor(map(u.mag(),0,width/2,3,12));
    noFill();
    beginShape();
    for(let i=0; i<n; i++) {
        let angle = map(i,0,n,0,TWO_PI);
        let half_angle = map(i+0.5,0,n,0,TWO_PI);
        vertex(radius*cos(angle), radius*sin(angle));
        vertex(inner_radius*cos(half_angle), inner_radius*sin(half_angle));
    }
    endShape(CLOSE);
}

function relativeMouse() {
    let mx = mouseX;
    let my = mouseY;
	let matrix = drawingContext.getTransform();
	let pd = pixelDensity();
    let rp = matrix.inverse().transformPoint(new DOMPoint(mx * pd,my * pd));
    return [ rp.x, rp.y ];
}
