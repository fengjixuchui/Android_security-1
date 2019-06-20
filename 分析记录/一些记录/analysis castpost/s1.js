Java.perform(function () {

    var FileClazz = Java.use("java.io.File");
    var class_exception = Java.use("java.lang.Exception");
    var class_log = Java.use("android.util.Log");

    console.log("Java.Use.Successfully!");

    var my_class = Java.use("fm.castbox.audio.radio.podcast.data.model.MeditationMusic");

    

    my_class.implementation = function( ){
        
        var str1 = this.title;
        console.log("[*] "+ str1);

    }



});