# Android Intent - Tutorial
https://www.vogella.com/tutorials/AndroidIntent/article.html

start another activity via an intent
Intent i = new Intent(this,ActivityTwo.class);
startActivity(i);

## Sending out explicit or implicit intents

Explicit intents
Intent i = new Intent(this, ActivityTwo.class);
i.putExtra("Value1","This value one for ActivityTwo");
i.putExtra("Value2","This value two ActivityTwo");

Implicit intents
Intent i = new Intent(Intent.ACTION_VIEW,Uri.parse("https://www.vogella.com/"));
startActivity(i);

## Determine valid intent receivers

'''
public static boolean isIntentAvailable(Context ctx,Intent intent){
	final PackageManager mgr = ctx.getPackageManager();
	List<ResolveInfo> list = 
		mgr.queryIntentActivities(intent,
			PackageManager.MATCH_DEFAULT_ONLY);
	return list.size() > 0;
}
'''

## Intents as eventtriggers

# Data transfer between activities
## Data transfer to the target component

'''
Bundle extras = getIntent().getExtras();
if (extras == null){
	return;
}
// get data via the key
String value1 = extras.getString(Intent.EXTRA_TEXT);
if(value1 != null){
	//do something with the data
}
'''

## Retrieving result data from a sub-activity

see it : startActivityForResult()

## Registering for intents via intent filters
but If a component does not define an intent filter,it can only be called by explicit intents.
'''
String url = "https://www.vogella.com"
Intent i = new Intent(Intent.ACTION_VIEW);
i.setData(Uri.parse(url));
startActivity(i);
'''

但Android系统如何识别可以对特定意图做出反应的组件？

组件可以通过意图过滤器为特定操作和特定数据注册自己。意图过滤器通过声明组件的功能来指定活动，服务或广播接收器可以响应的意图类型。

Android组件在AndroidManifest.xml中静态注册意图过滤器，或者在广播接收器的情况下也通过代码动态注册。意图过滤器由其类别，操作和数据过滤器定义。它还可以包含其他元数据。

如果将意图发送到Android系统，则Android平台会运行接收方确定。它使用意图中包含的数据。如果多个组件已注册相同的intent过滤器，则用户可以决定应该启动哪个组件。

您可以通过针对特定事件的intent过滤器注册Android组件。如果组件没有定义一个组件，则只能通过显式意图调用它。本章给出了为intent注册组件的示例。此注册的关键是您的组件注册正确的操作，mime-type并指定正确的元数据。

如果您将此类意图发送到您的系统，Android系统会为此意图确定所有已注册的Android组件。如果有几个组件已注册此意图，则用户可以选择应使用哪个组件。

1. Example
register an activity when someone wants to open a webpage.
'''
<activity android:name=".BrowserActivitiy"
          android:label="@string/app_name">
  <intent-filter>
     <action android:name="android.intent.action.VIEW" />
     <category android:name="android.intent.category.DEFAULT" />
     <data android:scheme="http"/>
  </intent-filter>
</activity>
'''

2. Example
registers an activity for ACTION_SEND intent. for text/plain mime type.
'''
<activity
    android:name=".ActivityTest"
    android:label="@string/app_name" >
    <intent-filter>
      <action android:name="android.intent.action.SEND" />

      <category android:name="android.intent.category.DEFAULT" />

      <data android:mimeType="text/plain" />

    </intent-filter>

</activity>
'''

# Pre-requistes for the following exercise
https://www.vogella.com/tutorials/Android/article.html#exercise_first_ui_interface

# Exercise: Activity communication with intents

# Exercise: Using the share intent

# Exercise: Picking an image via an intent

# Exercise: Register an activity as browser

# Exercise: Using different implicit intents

 