import{roundTo}from"../base/helpers.mjs";class Point{constructor(t,i){void 0===t&&(t=0),void 0===i&&(i=0),this.x=t,this.y=i}clone(){return new Point(this.x,this.y)}equals(t,i=0){return this.x-i<=t.x&&t.x<=this.x+i&&this.y-i<=t.y&&t.y<=this.y+i}copy(t){return this.x=t.x,this.y=t.y,this}subtract(t){return this.x-=t.x,this.y-=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}scale(t){this.x*=t,this.y*=t}distanceTo(t){return Math.sqrt(Math.pow(t.x-this.x,2)+Math.pow(t.y-this.y,2))}toString(){return`(${this.x},${this.y})`}rotate(t){let i=this.x,s=this.y;return this.x=i*Math.cos(t)-s*Math.sin(t),this.y=s*Math.cos(t)+i*Math.sin(t),this}}class Triplet{constructor(t,i,s){this.start=t,this.middle=i,this.end=s}orientation(){this.middle.y,this.start.y,this.end.x,this.middle.x,this.middle.x,this.start.x,this.end.y,this.middle.y;return 0===orientation?0:orientation>0?1:2}}class CardinalDirection{static NORTH=0;static NORTHEAST=1;static EAST=2;static SOUTHEAST=3;static SOUTH=4;static SOUTHWEST=5;static WEST=6;static NORTHWEST=7;static toName(t){return["North","Northeast","East","Southeast","South","Southwest","West","Northwest"][t]}}class Vector{constructor(t,i){this.start=t,this.end=i}get actualCardinal(){let t=180*Math.atan2(this.end.y-this.start.y,this.end.x-this.start.x)/Math.PI+180,i=roundTo(t,45),s=parseInt(i/45)-2;return s<0&&(s+=7),s}estimateCardinal(t=0){let i=this.start.x-t<=this.end.x&&this.end.x<=this.start.x+t;return this.start.y-t<=this.end.y&&this.end.y<=this.start.y+t?this.end.x>this.start.x?CardinalDirection.EAST:CardinalDirection.WEST:i?this.end.y>this.start.y?CardinalDirection.SOUTH:CardinalDirection.NORTH:this.end.x>this.start.x?this.end.y>this.start.y?CardinalDirection.SOUTHEAST:CardinalDirection.NORTHEAST:this.end.y>this.start.y?CardinalDirection.SOUTHWEST:CardinalDirection.NORTHWEST}get deltaX(){return this.end.x-this.start.x}get deltaY(){return this.end.y-this.start.y}get magnitude(){return this.start.distanceTo(this.end)}get halfway(){return new Point((this.start.x+this.end.x)/2,(this.start.y+this.end.y)/2)}onVector(t){return t.x<=Math.max(this.start.x,this.end.x)&&t.x>=Math.max(this.start.x,this.end.x)&&t.y<=Math.max(this.start.y,this.end.y)&&t.y>=Math.min(this.start.y,this.end.y)}intersects(t){let i=[new Triplet(this.start,this.end,t.start),new Triplet(this.start,this.end,t.end),new Triplet(t.start,t.end,this.start),new Triplet(t.start,t.end,this.end)].map((t=>t.orientation()));return i[0]!==i[1]&&i[2]!==i[3]||(!(0!==i[0]||!this.onVector(t.start))||(!(0!==i[1]||!this.onVector(t.end))||(!(0!==i[2]||!t.onVector(this.start))||!(0!==i[3]||!t.onVector(this.end)))))}}class Drawable{constructor(t){this.points=t,this.points.sort(((t,i)=>t.x-i.x)),this.center=t.slice(1).reduce(((t,i)=>(t.x+=i.x,t.y+=i.y,t)),this.points[0].clone()),this.center.x/=this.points.length,this.center.y/=this.points.length,this.minimum=this.getMinimum(),this.maximum=this.getMaximum()}clone(){return new Drawable([].concat(this.points.map((t=>t.clone()))))}getMaximum(){return new Point(Math.max(...this.points.map((t=>t.x))),Math.max(...this.points.map((t=>t.y))))}getMinimum(){return new Point(Math.min(...this.points.map((t=>t.x))),Math.min(...this.points.map((t=>t.y))))}translateX(t){for(let i of this.points)i.x+=t;return this.center.x+=t,this}translateY(t){for(let i of this.points)i.y+=t;return this.center.y+=t,this}get bounds(){let t=this.minimum,i=this.maximum;return[t.x,t.y,i.x-t.x,i.y-t.y]}get extremes(){let t=this.minimum,i=this.maximum;return[new Point(t.x,t.y),new Point(i.x,t.y),new Point(i.x,i.y),new Point(t.x,i.y)]}containsBounding(t,i=!0){let s=this.minimum,e=this.maximum;return i?s.x<=t.x&&t.x<=e.x&&s.y<=t.y&&t.y<=e.y:s.x<t.x&&t.x<e.x&&s.y<t.y&&t.y<e.y}contains(t){let i,s,e=new Vector(t,new Point(1/0,t.y));return i=1%this.length,s=new Vector(this.points[0],this.points[i]),s.intersects(e)&&0===new Triplet(this.points[0],t,this.points[i]).orientation()?s.onVector(t):0}translate(t){for(let i of this.points)i.x+=t.deltaX,i.y+=t.deltaY;return this.center.x+=t.deltaX,this.center.y+=t.deltaY,this}rotate(t){return this.rotateAbout(t,this.center)}rotateAbout(t,i){let s;for(let e of this.points)s=e.clone().subtract(i),s.rotate(t),s.add(i),e.copy(s);return this}scale(t){return this.scaleAbout(t,this.center)}scaleAbout(t,i){let s;for(let e of this.points)s=e.clone().subtract(i),s.scale(t),s.add(i),e.copy(s);return this}drawPath(t){t.beginPath(),t.moveTo(this.points[0].x,this.points[0].y);for(let i of this.points.slice(1))t.lineTo(i.x,i.y)}stroke(t){this.drawPath(t),t.stroke()}fill(t){this.drawPath(t),t.fill()}}export{Point,Vector,Drawable,CardinalDirection};
