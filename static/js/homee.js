console.log("javascript is running")
var swichButtonMonthly = document.getElementById("swichButtonMonthly");
var swichButtonYearly = document.getElementById("swichButtonYearly");
var planCards = document.getElementById("planCards");
window.onload = clickMonthly;
swichButtonMonthly.onclick =clickMonthly;
swichButtonYearly.onclick = clickYearly;

function clickMonthly() {
  swichButtonMonthly.className="active switchBtn";
  swichButtonYearly.className="switchBtn";
  planCards.innerHTML = `<div class="card">
  <p class="cardHeading">Basic</p>
  <p class="cardHeading">1000</p>
  <span style="text-align: center;">Billed monthly</span>
  <a href="" class="cardButton">Start Your Free Trial Now</a>
  <div class="cardDetails">
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
          doctor, tpa and patient app</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
  </div>
</div>
<div class="card">
  <p class="cardHeading">Standard</p>
  <p class="cardHeading">1000</p>
  <span style="text-align: center;">Billed monthly</span>
  <a href="" class="cardButton">Buy Now</a>
  <div class="cardDetails">
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
          doctor, tpa and patient app</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
  </div>
</div>
<div class="card">
  <p class="cardHeading">Premium</p>
  <p class="cardHeading">1000</p>
  <span style="text-align: center;">Billed monthly</span>
  <a href="" class="cardButton">Buy Now</a>
  <div class="cardDetails">
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
          doctor, tpa and patient app</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
  </div>
</div>
<div class="card">
  <p class="cardHeading">Platinum</p>
  <p class="cardHeading">1000</p>
  <span style="text-align: center;">Billed monthly</span>
  <a href="" class="cardButton">Buy Now</a>
  <div class="cardDetails">
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
          doctor, tpa and patient app</p>
      <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
  </div>
</div>`;
};

function clickYearly() {
    swichButtonMonthly.className="switchBtn";
    swichButtonYearly.className="active switchBtn";

    planCards.innerHTML=`<div class="card">
    <p class="cardHeading">Basic</p>
    <p class="cardHeading">1000</p>
    <span style="text-align: center;">Billed monthly</span>
    <a href="" class="cardButton">Start Your Free Trial Now</a>
    <div class="cardDetails">
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
            doctor, tpa and patient app</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
    </div>
  </div>
  <div class="card">
    <p class="cardHeading">Standard</p>
    <p class="cardHeading">1000</p>
    <span style="text-align: center;">Billed monthly</span>
    <a href="" class="cardButton">Buy Now</a>
    <div class="cardDetails">
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
            doctor, tpa and patient app</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
    </div>
  </div>
  <div class="card">
    <p class="cardHeading">Premium</p>
    <p class="cardHeading">1000</p>
    <span style="text-align: center;">Billed monthly</span>
    <a href="" class="cardButton">Buy Now</a>
    <div class="cardDetails">
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Claims management desk</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Electronic pre auth form generation</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Training and customer support</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">preauth form generate remotly with integrated
            doctor, tpa and patient app</p>
        <p><img src="./imgs/greenTick.png" height="15px" alt="">Integrated email console</p>
    </div>
  </div>`
};

