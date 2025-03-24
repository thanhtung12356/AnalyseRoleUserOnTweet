import pandas as pd

df1 = pd.read_csv("D:\\ImportBackUp\\WORKSPACE\\DoAnPTMXH\\Twitter-dataset\\data\\nodes.csv", header=None, names=["profile_id"])  # Đọc file1 (danh sách id)
df2 = pd.read_csv("D:\ImportBackUp\WORKSPACE\DoAnPTMXH\Twitter-dataset\data\edges.csv", header=None, names=["source", "target"])  # Đọc file2 (danh sách quan hệ giữa id)

# Chọn 2.5% hàng từ file1
sampled_ids = set(df1.sample(frac=0.025, random_state=42)["profile_id"])  # Lấy 2.5% id từ file1

# Lọc dữ liệu trong file2 sao cho chỉ giữ lại các hàng liên quan đến sampled_ids
filtered_df2 = df2[(df2["source"].isin(sampled_ids)) & (df2["target"].isin(sampled_ids))]

# Đảm bảo các id trong filtered_df2 vẫn xuất hiện trong file1
final_df1 = df1[df1["profile_id"].isin(filtered_df2["source"]) | df1["profile_id"].isin(filtered_df2["target"])]

# Lưu kết quả ra file CSV mới
final_df1.to_csv("extract_nodes.csv", index=False, header=False)
filtered_df2.to_csv("extract_edges.csv", index=False, header=False)

print("Đã lưu file filtered_file1.csv và filtered_file2.csv với 2.5% dữ liệu giữ nguyên tính nhất quán.")
