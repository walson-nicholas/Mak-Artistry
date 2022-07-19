$(document).ready(function(){
    
    (function() {
        const nav = document.getElementById('nav');
        const anchor = nav.getElementsByTagName('a');
        const current = window.location.pathname.split('/')[1];
        for (let i = 0; i < anchor.length; i++) {
            if(anchor[i].href.includes(current) && current !== '') {
                anchor[i].classList.add('active');
            }else if(current === ''){
                anchor[0].classList.add('active');
                anchor[1].classList.remove('active');
            }else{
                anchor[i].classList.remove('active');
            }
        }
    })();
    
    
    if ($(window).width() < 600){
        console.log('width is less than 600px')
    
        $("#searchIcon").click(function(){
            $(".navIcons a").css("display", "none");
            $("#burger").css("margin-right", "0");
            $("#searchBar").css("display", "flex");
        });
        
        $("#searchBarSubmit").click(function(){
            $("#searchBar").css("display", "none");
            $("#burger").css("margin-right", "8vw");
            $(".navIcons a").css("display", "inline-block");
        });        
        
    } else{
        console.log('width is greater than 600px')
        
        $("#searchIcon").click(function(){
            $("#searchIcon").css("display", "none");
            $("#searchBar").css("display", "flex");
        });
        
        $("#searchBarSubmit").click(function(){
            $("#searchBar").css("display", "none");
            $("#searchIcon").css("display", "inline-block");
        });
    
    }
    
    
    $(".toggler").click(function(){
        $("#searchIcon").toggleClass("whiteSearch");
    });

})