let fr = 15;
let grid;
let world;
let rows,cols;
let res = 100;
let flag = 0;

class Cell{
    constructor(i,j,res){
        this.i = i;
        this.j = j;
        this.x = this.i*res;
        this.y = this.j*res;
        this.state = 0;
    }
    
    clicked(mx,my){
        if(this.x<mx && mx<this.x+res && this.y<my && my<this.y+res){
            if(this.state == 0){
                this.state = 1;
            }
            else{
                this.state = 0;
            }
        }
    }

    show(){
        if(this.state == 1){
            fill(0,255,0);
            stroke(0);
            rect(this.x,this.y,res-1,res-1);
        }
    }
}

function initialize_world(){
    let arr = new Array(cols);
    for(let i = 0;i<arr.length;i++){
        arr[i] = new Array(rows);
    }
    return arr;
}

function mousePressed() {
    for(let i=0;i<cols;i++) {
        for(let j=0;j<rows;j++){
            world[i][j].clicked(mouseX, mouseY);
        }
    }
}

function reset_world(){
    flag = 0;
}

function apocalypse(){
    world = initialize_world();
    for(let i=0;i<cols;i++){
        for(let j=0;j<rows;j++){
            world[i][j] = new Cell(i,j,res);
        }
    }
}

function transposeArray(array, arrayLength){
    var newArray = [];
    for(var i = 0; i < array.length; i++){
        newArray.push([]);
    };

    for(var i = 0; i < array.length; i++){
        for(var j = 0; j < arrayLength; j++){
            newArray[j].push(array[i][j]);
        };
    };

    return newArray;
}

function simulate(){
    grid = initialize_world();
    for(let i=0;i<cols;i++){
        for(let j=0;j<rows;j++){
            grid[i][j] = world[i][j].state;
        }
    }

    // Blue Grid neighbourhood
    let blue_grid = new Array(cols/2);
    for(let i = 0;i<blue_grid.length;i++){
        blue_grid[i] = new Array(rows/2);
    }
    for(let i=0;i<cols/2;i++){
        for(let j=0;j<rows/2;j++){
            blue_grid[i][j] = 0;
        }
    }

    console.table(transposeArray(blue_grid,blue_grid.length));
    console.log(transposeArray(grid,grid.length));
    
    flag = 1;
}

function setup(){
    createCanvas(800,800);
    frameRate(fr);
    cols = width/res;
    rows = height/res;
    console.log(cols);
    console.log(rows);
    apocalypse();
    let simulate_button = createButton("Simulate");
    simulate_button.mousePressed(simulate);
    let reset_button = createButton("Reset");
    reset_button.mousePressed(reset_world);
}

function draw(){
    background(0);
    if(flag == 0){
        for(let i=0;i<cols;i++){
            for(let j=0;j<rows;j++){
                let x = i * res;
                let y = j * res;
                if(world[i][j].state == 1){
                    world[i][j].show();
                }
            }    
        }
    }
    else{
        for(let i=0;i<cols;i++){
            for(let j=0;j<rows;j++){
                let x = i * res;
                let y = j * res;
                if(grid[i][j]==1){
                    fill(0,255,0);
                    stroke(0);
                    rect(x,y,res-1,res-1);
                }
            }    
        } 
    }
}


