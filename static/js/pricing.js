var swichButtonMonthly = document.getElementById("swichButtonMonthly");
var swichButtonYearly = document.getElementById("swichButtonYearly");
var planCards = document.getElementById("planCards");
window.onload = clickMonthly;

var myplans = document.getElementById('myplans').value;
console.log(myplans);
var myplansArr = myplans.split(',');
console.log(myplansArr);

function clickMonthly() {
  swichButtonMonthly.className = "active switchBtn";
  swichButtonYearly.className = "switchBtn";
  planCards.innerHTML = `
  <div class="card">
        <p class="cardHeading">Free Trial</p>
        <p class="cardHeading" style="margin-bottom:45px">${myplansArr[0]} INR</p>
        <span style="text-align: center; ">Billed monthly</span>
        <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;"
        >Start Your Free Trial Now</a> <br>
        <div class="cardDetails">
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Electronic
            pre auth form generation
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Training and
            customer support
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Get access to
            our Doctor TPA and Patient App (15-Claims)
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Integrated
            email console
          </p>
          <p>
            Subscribe & Try all product features for free for 15 days or upto 15
            Claims. After 15 claims you will be charged INR 200 per claim
          </p>
        </div>
      </div>
      <div class="card" style="text-align: center">
        <p class="cardHeading">Standard</p>
       
        <p class="cardHeading">${myplansArr[1]} INR</p>
        <p style="text-align:center;color:red"><strike> 4000</strike> INR  10% off </p>
        <span style="text-align: center">Billed monthly</span>
        <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
        <div class="cardDetails">
        <p>
          <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Upto 20
          Electronic Pre-auth form generation (20-Claims)
        </p>
        <p>
          <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Training and
          customer support
        </p>
        <p>
          <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Get access to
          our Doctor TPA and Patient App (20-Claims)
        </p>
        <p>
          <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Integrated
          email console
        </p>
        <p>
          Subscribe and get upto 20 claims. On additional cases after your
          plan exhaust INR 200 per claim
        </p>
      </div>
      </div>
      <div class="card">
        <p class="cardHeading">Premium</p>
        <p class="cardHeading">${myplansArr[2]} INR</p>
        <p style="text-align:center;color:red"><strike> 10000</strike> INR  15% off </p>
        <span style="text-align: center">Billed monthly</span>
        <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
        <div class="cardDetails">
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Upto 50
            Electronic Pre-auth form generation
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Training and
            customer support
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Get access to
            our Doctor TPA and Patient App
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Integrated
            email console
          </p>
          <p>
            Subscribe and get upto 50 claims. On additional cases after your
            plan exhaust INR 200 per claim
          </p>
        </div>
      </div>
      </div>
      <div class="card">
        <p class="cardHeading">Platinum</p>
        <p class="cardHeading">${myplansArr[3]} INR</p>
        <p style="text-align:center;color:red"><strike> 20000</strike> INR  20% off </p>
        <span style="text-align: center">Billed monthly</span>
        <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
        <div class="cardDetails">
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Upto 100
            Electronic Pre-auth form generation
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Training and
            customer support
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Get access to
            our Doctor TPA and Patient App
          </p>
          <p>
            <img src="../static/imgs/greenTick.png" height="15px" alt="" /> Integrated
            email console
          </p>
          <p>
            Subscribe and get upto 100 claims. On additional cases after your
            plan exhaust INR 200 per claim
          </p>
        </div>
      </div>
    
  `;
}

function clickYearly() {
  swichButtonMonthly.className = "switchBtn";
  swichButtonYearly.className = "active switchBtn";

  planCards.innerHTML = `
  <div class="card">
    <p class="cardHeading">Standard</p>
    <p class="cardHeading">${myplansArr[4]} INR</p>
    <p style="text-align:center;color:red"><strike> 48000</strike> INR  15% off </p>
    <span style="text-align: center;">Billed yearly</span>
    <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
    <div class="cardDetails">
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Upto 240 Electronic Pre-auth form generation</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Training and customer support</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Get access to our Doctor TPA and Patient App(240 claims)</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Integrated email console</p>
    </div>
  </div>
  <div class="card">
    <p class="cardHeading">Premium</p>
    <p class="cardHeading">${myplansArr[5]} INR</p>
    <p style="text-align:center;color:red"><strike> 120000</strike> INR  20% off </p>
    <span style="text-align: center;">Billed yearly</span>
    <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
    <div class="cardDetails">
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Upto 600 Electronic Pre-auth form generation</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Training and customer support</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Get access to our Doctor TPA and Patient App (600 claims)</p>
        <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Integrated email console</p>
    </div>
  </div>
  <div class="card" style="text-align:center;">
  <p class="cardHeading">Platinum</p>
  <p class="cardHeading">${myplansArr[6]} INR</p>
  <p style="text-align:center;color:red"><strike> 240000</strike> INR  27% off </p>
  <span style="text-align: center;">Billed yearly</span>
  <a href="afterPricehospitalDetail" class="cardButton" style=" background-color: #fc8c03;">Buy Now</a><br>
  <div class="cardDetails">
  <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Upto 1200 Electronic Pre-auth form generation</p>
  <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Training and customer support</p>
  <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Get access to our Doctor TPA and Patient App (1200 claims)</p>
  <p><img src="../static/imgs/greenTick.png" height="15px" alt=""> Integrated email console</p>
</div>
</div>
  `;
}

{/* <div class="card" style="text-align:center;">
    <p class="cardHeading">Add on</p>
    <a href="afterPricehospitalDetail" class="cardButton">Add on</a>
    <div class="cardDetails">
    <br>
    <br>

        <p>Get your add on pack and process claims as per your requirement in just
        INR 125 on each case
        </p>
    </div>
  </div> */}