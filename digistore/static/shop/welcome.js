
if(document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', afterLoaded);
}
else{
    afterLoaded();
    
}
function afterLoaded(){


    document.getElementById('signUp').addEventListener('click', function(){
        document.getElementById('container').classList.add('right-panel-active')
    });
    
    
    document.getElementById('signIn').addEventListener('click', function()
    {
        document.getElementById('container').classList.remove('right-panel-active')
    });

}