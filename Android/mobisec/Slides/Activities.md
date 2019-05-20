# Activities

## configuring the manifest

* declare activities
'''
	<manifest ...>
		<application ...>
			<activity android:name=".ExampleActivity" />
			...
		</application ...>
		...
	</manifest>
'''

至少需要声明 android:name 这个属性

* decalre intent filters
'''
	<activity android:name=".ExampleActivity" android:icon="@drawable/app_icon">
	    <intent-filter>
	        <action android:name="android.intent.action.SEND" />
	        <category android:name="android.intent.category.DEFAULT" />
	        <data android:mimeType="text/plain" />
	    </intent-filter>
	</activity>
'''

declaring <intent-filter> in <activity>.in the attr, include <action>, opt <category> and/or <data>

call the activity described above (如果我只想自己启动呢，用显示启动就行，不需要声明任何隐式启动)
1. 
'''Java
// Create the text message with a string
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.setType("text/plain");
sendIntent.putExtra(Intent.EXTRA_TEXT, textMessage);
// Start the activity
startActivity(sendIntent);
'''

2. kotlin
'''
val sendIntent = Intent().apply {
    action = Intent.ACTION_SEND
    type = "text/plain"
    putExtra(Intent.EXTRA_TEXT, textMessage)
}
startActivity(sendIntent)
'''

* declare permissions
parent activity cannot launch a child activity unless both activities have the same permissions in their manifest.If you declare a <uses-permission> element for a particular activity, the calling activity must have a matching <uses-permission> element.

For example, if your app wants to use a hypothetical app named SocialApp to share a post on social media, SocialApp itself must define the permission that an app calling it must have:

A app -> use B app to share a post on social media. B app must define :
'''
<manifest>
<activity android:name="...."
   android:permission=”com.google.socialapp.permission.SHARE_POST”

/>
'''

A app must define : 
'''
<manifest>
   <uses-permission android:name="com.google.socialapp.permission.SHARE_POST" />
</manifest>
'''

## activity lifecycle

callbacks to handle transitions between states.

* onCreate()
activity 基础callback。用于初始化activity，触发activity。you must call setContentView() to define the layout for the activity's user interface。

* onStart()
activity 进入 Started 状态。并且activity可见了。此回调包含活动最终准备到达前台并变为交互式的内容。

* onResume()
system invokes this callback. before activity starts 与用户交互。
如此，this activity at the top of the activity stack，捕获user 所有 input。应用程序的大多数核心功能都是在onResume（）方法中实现的。

* onPause()
1. 当activity 不被关注，system call onPause()暂停 activity。技术上来说，activity仍然可见，只是user离开了这个activity。activity将马上停止或者Resume。
2. An activity in the Paused state may continue to update the UI if the user is expecting the UI to update
3. 我们不需要调用onPause()

* onStop()
当 用户许久不使用activity。
1. activity being destroyed，
2. new activity is starting，
3. or an existing activity entring a Resumed state，covering stopped activity。

* onRestart()
system invokes this callback.when activity in Stopped state.
it will restores the state of activity from the time that it was stopped.

* onDestroy()
system invokes this callback vefore an activity is destroyed.
finnal onw activity receives.
活动或包含它的进程被销毁时释放所有活动的资源。