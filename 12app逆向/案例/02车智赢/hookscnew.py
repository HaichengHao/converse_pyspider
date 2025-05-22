import frida
import sys

def on_message(message, data):
    print("[*] Message:", message)

# 获取远程设备
device = frida.get_remote_device()

# 自动查找主进程 PID
processes = device.enumerate_processes()
target_process = None

for process in processes:
    # 检查进程名是否为主进程名（不包含冒号）
    if "com.che168.autotradercloud" == process.name and ":" not in process.name:
        target_process = process
        break

if not target_process:
    print("❌ 未找到目标应用的主进程，请确保 App 已启动！")
    exit(1)

print(f"✅ 找到主进程：{target_process.name} (PID={target_process.pid})")

# Attach 到主进程
session = device.attach(target_process.pid)

# Frida Hook 脚本（添加 Java.available 检查）
hook_code = """
if (Java.available) {
    console.log("✅ 当前为 Android 环境，开始 Hook...");

    Java.perform(function () {
        try {
            var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");

            UserModel.loginByPassword.implementation = function(str, str2, str3, callback) {
                console.log("Hooked loginByPassword:", str, str2, str3);
                this.loginByPassword(str, str2, str3, callback);
            }
        } catch (e) {
            console.log("❌ Hook 失败：", e.message);
        }
    });
} else {
    console.log("❌ 当前不是 Android 环境，无法使用 Java API！");
}
"""

script = session.create_script(hook_code)
script.on("message", on_message)
script.load()

print("🚀 Hook 注入成功，按 Ctrl+C 停止...")
sys.stdin.read()