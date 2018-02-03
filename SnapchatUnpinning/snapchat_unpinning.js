Java.perform(function () {

    console.log('[*] Script started');
    
    const certificateArray = Java.use('[Ljava.lang.String;');
    const JavaString = Java.use('java.lang.String');
    var myCertificate = null;

    recv('input', function(value) {
        myCertificate = JavaString.$new(value.payload);
    });
    
    var HookedClass = Java.use('java.security.cert.CertificateFactory');
    const InputStream = Java.use('java.io.ByteArrayInputStream');
    var inStreamCertificate = InputStream.$new(myCertificate.getBytes());

    var done = false;

    HookedClass.generateCertificate.implementation = function (inStream) {
        
        if(!done) { // we will change only the first certificate to ours
            console.log("[*] Successfully changed the certificate");
            done = true;
            return this.generateCertificate(inStreamCertificate);
        }
        return this.generateCertificate(inStream);
    }; 
});