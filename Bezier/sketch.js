let p1, p2, p3, p4, A, B, C, D, E, F, t, n;
let bool;
function interpolar(p1,p2,t){
    let x,y;
    let p3 ={x,y};
    p3.x=(1-t)*p1.x+p2.x*t;
    p3.y=(1-t)*p1.y+p2.y*t;
    return p3;
}
function marcaPonto(ponto){
    fill("black");
    circle(ponto.x,ponto.y,5);
}
function pontoInterativo(ponto){
    //fill("black");
    noFill();
    if(mouseOver(ponto)){
        fill("red");
        if(mouseIsPressed){
            ponto.x=mouseX;
            ponto.y=mouseY;
        }
    }
    circle(ponto.x,ponto.y,5);
}
function modulo(x){
    if(x<0){return -x}
    return x;
}
function mouseOver(ponto){
    if(modulo(mouseX-ponto.x)<20&&modulo(mouseY-ponto.y)<20){
        return true;
    }
    return false;
}
function setup(){
    createCanvas(1920,1000);
    t=[];
    n = 50;
    for(let i=0;i<n;i++){
        t[i]=i/n;
    }
    frameRate(240);
    p1 = {x:460,y:height/2};
    p2 = {x:1460,y:height/2};
    p3 = {x:910,y:50};
    p4 = {x:1010,y:50}
}
function draw(){
    background(200);
    pontoInterativo(p1);
    pontoInterativo(p2);
    pontoInterativo(p3);
    pontoInterativo(p4);
    for(let i=1;i<t.length;i++){
        A = interpolar(p1,p3,t[i]);
        B = interpolar(p4,p2,t[i]);
        C = interpolar(p3,p4,t[i]);
        D = interpolar(A,C,t[i]);
        E = interpolar(C,B,t[i]);
        F = interpolar(D,E,t[i]);
        marcaPonto(F);
    }
}
