#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0) {
        // If w or h is not a positive integer or equal to 0, create an empty object
        return {};
      } else {
        this.width = w;
        this.height = h;
      }
    }
  
    print() {
        if (this.width < 0 || this.height < 0) {
            console.log('');
        }else {
            for (let i = 0; i < this.width; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }
}

module.exports = Rectangle;