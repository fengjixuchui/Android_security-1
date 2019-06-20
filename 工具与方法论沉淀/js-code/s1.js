Java.perform(function () {

    var FileClazz = Java.use("java.io.File");
    var class_exception = Java.use("java.lang.Exception");
    var class_log = Java.use("android.util.Log");

    console.log("Java.Use.Successfully!");

    var my_class = Java.use("com.airbnb.lottie.f");

    
    // callback
    function backtrace(){
        var my_exception_obj = class_exception.$new();
        trace = class_log.getStackTraceString(my_exception_obj);  
        console.log(trace);
    }


    my_class.b.overload('java.util.zip.ZipInputStream', 'java.lang.String').implementation = function(  x, y ){
        // 
        console.log("seekTo hooked, time is " + x.toString())

    }



});