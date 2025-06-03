from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
import csv

# Initialize FastMCP server
mcp = FastMCP("demo")

@mcp.tool()
async def get_products_from_csv() -> str:
    """
    Get list of products at store.
    """

    csv_path = os.path.join(os.path.dirname(__file__), "products_data.csv")

    if not os.path.isfile(csv_path):
        return "Không tìm thấy file products_data.csv."

    try:
        result = []
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = f"""
                Tên sản phẩm: {row.get("name", "Không rõ")}
                Giá: {row.get("price", "Không rõ")} VND
                Thương hiệu: {row.get("brand", "Không rõ")}
                Xuất xứ: {row.get("country_of_origin", "Không rõ")}
                Danh mục: {row.get("category", "Không rõ")}
                """
                result.append(item.strip())
        return "\n---\n".join(result) if result else "Không có sản phẩm nào trong file CSV."
    except Exception as e:
        return f"Lỗi khi đọc file CSV: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
