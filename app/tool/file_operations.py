"""
File operations tool providing comprehensive file and directory management capabilities.
This tool complements the str_replace_editor with additional file operations.
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional, Union

from app.tool.base import BaseTool, ToolResult


class FileOperations(BaseTool):
    """A tool for comprehensive file and directory operations."""
    
    name: str = "file_operations"
    description: str = """Comprehensive file and directory operations tool.
    Supports operations like copying, moving, deleting files and directories,
    changing permissions, getting file info, and more. Use this for file system
    operations that go beyond basic reading/writing/editing."""
    
    parameters: dict = {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": [
                    "list_directory",
                    "create_directory", 
                    "copy_file",
                    "copy_directory",
                    "move_file", 
                    "move_directory",
                    "delete_file",
                    "delete_directory",
                    "get_file_info",
                    "change_permissions",
                    "find_files",
                    "get_file_size",
                    "get_directory_size"
                ],
                "description": "The file operation to perform"
            },
            "path": {
                "type": "string", 
                "description": "The file or directory path to operate on"
            },
            "destination": {
                "type": "string",
                "description": "Destination path for copy/move operations"
            },
            "pattern": {
                "type": "string", 
                "description": "Search pattern for find_files operation (supports wildcards like *.py)"
            },
            "recursive": {
                "type": "boolean",
                "description": "Whether to perform operation recursively (for applicable operations)",
                "default": False
            },
            "permissions": {
                "type": "string",
                "description": "Permissions in octal format (e.g., '755') for change_permissions operation"
            },
            "show_hidden": {
                "type": "boolean", 
                "description": "Whether to show hidden files in directory listings",
                "default": False
            }
        },
        "required": ["operation", "path"]
    }

    async def execute(
        self,
        operation: str,
        path: str,
        destination: Optional[str] = None,
        pattern: Optional[str] = None,
        recursive: bool = False,
        permissions: Optional[str] = None,
        show_hidden: bool = False,
        **kwargs
    ) -> ToolResult:
        """Execute the specified file operation."""
        try:
            path_obj = Path(path)
            
            if operation == "list_directory":
                return await self._list_directory(path_obj, show_hidden, recursive)
            
            elif operation == "create_directory":
                return await self._create_directory(path_obj, recursive)
            
            elif operation == "copy_file":
                if not destination:
                    return ToolResult(error="Destination path required for copy_file operation")
                return await self._copy_file(path_obj, Path(destination))
            
            elif operation == "copy_directory":
                if not destination:
                    return ToolResult(error="Destination path required for copy_directory operation")
                return await self._copy_directory(path_obj, Path(destination))
            
            elif operation == "move_file":
                if not destination:
                    return ToolResult(error="Destination path required for move_file operation")
                return await self._move_file(path_obj, Path(destination))
            
            elif operation == "move_directory":
                if not destination:
                    return ToolResult(error="Destination path required for move_directory operation")
                return await self._move_directory(path_obj, Path(destination))
            
            elif operation == "delete_file":
                return await self._delete_file(path_obj)
            
            elif operation == "delete_directory":
                return await self._delete_directory(path_obj, recursive)
            
            elif operation == "get_file_info":
                return await self._get_file_info(path_obj)
            
            elif operation == "change_permissions":
                if not permissions:
                    return ToolResult(error="Permissions parameter required for change_permissions operation")
                return await self._change_permissions(path_obj, permissions)
            
            elif operation == "find_files":
                if not pattern:
                    return ToolResult(error="Pattern parameter required for find_files operation")
                return await self._find_files(path_obj, pattern, recursive)
            
            elif operation == "get_file_size":
                return await self._get_file_size(path_obj)
            
            elif operation == "get_directory_size":
                return await self._get_directory_size(path_obj)
            
            else:
                return ToolResult(error=f"Unknown operation: {operation}")
                
        except Exception as e:
            return ToolResult(error=f"File operation '{operation}' failed: {str(e)}")

    async def _list_directory(self, path: Path, show_hidden: bool, recursive: bool) -> ToolResult:
        """List directory contents."""
        if not path.exists():
            return ToolResult(error=f"Directory does not exist: {path}")
        
        if not path.is_dir():
            return ToolResult(error=f"Path is not a directory: {path}")
        
        items = []
        try:
            if recursive:
                for item in path.rglob("*"):
                    if show_hidden or not item.name.startswith('.'):
                        rel_path = item.relative_to(path)
                        item_type = "directory" if item.is_dir() else "file"
                        size = item.stat().st_size if item.is_file() else "-"
                        items.append(f"{item_type:10} {size:>10} {rel_path}")
            else:
                for item in path.iterdir():
                    if show_hidden or not item.name.startswith('.'):
                        item_type = "directory" if item.is_dir() else "file"  
                        size = item.stat().st_size if item.is_file() else "-"
                        items.append(f"{item_type:10} {size:>10} {item.name}")
            
            output = f"Contents of {path}:\n"
            output += f"{'Type':10} {'Size':>10} Name\n"
            output += "-" * 50 + "\n"
            output += "\n".join(sorted(items))
            
            return ToolResult(output=output)
            
        except PermissionError:
            return ToolResult(error=f"Permission denied accessing directory: {path}")

    async def _create_directory(self, path: Path, recursive: bool) -> ToolResult:
        """Create a directory."""
        try:
            if path.exists():
                return ToolResult(error=f"Directory already exists: {path}")
            
            if recursive:
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.mkdir()
            
            return ToolResult(output=f"Directory created: {path}")
        except Exception as e:
            return ToolResult(error=f"Failed to create directory {path}: {str(e)}")

    async def _copy_file(self, source: Path, destination: Path) -> ToolResult:
        """Copy a file."""
        try:
            if not source.exists():
                return ToolResult(error=f"Source file does not exist: {source}")
            
            if not source.is_file():
                return ToolResult(error=f"Source is not a file: {source}")
            
            # Create destination directory if it doesn't exist
            destination.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(source, destination)
            return ToolResult(output=f"File copied from {source} to {destination}")
        except Exception as e:
            return ToolResult(error=f"Failed to copy file: {str(e)}")

    async def _copy_directory(self, source: Path, destination: Path) -> ToolResult:
        """Copy a directory."""
        try:
            if not source.exists():
                return ToolResult(error=f"Source directory does not exist: {source}")
            
            if not source.is_dir():
                return ToolResult(error=f"Source is not a directory: {source}")
            
            if destination.exists():
                return ToolResult(error=f"Destination already exists: {destination}")
            
            shutil.copytree(source, destination)
            return ToolResult(output=f"Directory copied from {source} to {destination}")
        except Exception as e:
            return ToolResult(error=f"Failed to copy directory: {str(e)}")

    async def _move_file(self, source: Path, destination: Path) -> ToolResult:
        """Move a file."""
        try:
            if not source.exists():
                return ToolResult(error=f"Source file does not exist: {source}")
            
            # Create destination directory if it doesn't exist
            destination.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.move(source, destination)
            return ToolResult(output=f"File moved from {source} to {destination}")
        except Exception as e:
            return ToolResult(error=f"Failed to move file: {str(e)}")

    async def _move_directory(self, source: Path, destination: Path) -> ToolResult:
        """Move a directory."""
        try:
            if not source.exists():
                return ToolResult(error=f"Source directory does not exist: {source}")
            
            if not source.is_dir():
                return ToolResult(error=f"Source is not a directory: {source}")
            
            shutil.move(source, destination)
            return ToolResult(output=f"Directory moved from {source} to {destination}")
        except Exception as e:
            return ToolResult(error=f"Failed to move directory: {str(e)}")

    async def _delete_file(self, path: Path) -> ToolResult:
        """Delete a file."""
        try:
            if not path.exists():
                return ToolResult(error=f"File does not exist: {path}")
            
            if not path.is_file():
                return ToolResult(error=f"Path is not a file: {path}")
            
            path.unlink()
            return ToolResult(output=f"File deleted: {path}")
        except Exception as e:
            return ToolResult(error=f"Failed to delete file: {str(e)}")

    async def _delete_directory(self, path: Path, recursive: bool) -> ToolResult:
        """Delete a directory."""
        try:
            if not path.exists():
                return ToolResult(error=f"Directory does not exist: {path}")
            
            if not path.is_dir():
                return ToolResult(error=f"Path is not a directory: {path}")
            
            if recursive:
                shutil.rmtree(path)
                return ToolResult(output=f"Directory and contents deleted: {path}")
            else:
                path.rmdir()  # Only works if directory is empty
                return ToolResult(output=f"Empty directory deleted: {path}")
        except Exception as e:
            return ToolResult(error=f"Failed to delete directory: {str(e)}")

    async def _get_file_info(self, path: Path) -> ToolResult:
        """Get detailed information about a file or directory."""
        try:
            if not path.exists():
                return ToolResult(error=f"Path does not exist: {path}")
            
            stat = path.stat()
            info = [
                f"Path: {path}",
                f"Type: {'Directory' if path.is_dir() else 'File'}",
                f"Size: {stat.st_size} bytes",
                f"Created: {stat.st_ctime}",
                f"Modified: {stat.st_mtime}",
                f"Accessed: {stat.st_atime}",
                f"Permissions: {oct(stat.st_mode)[-3:]}",
                f"Owner UID: {stat.st_uid}",
                f"Group GID: {stat.st_gid}"
            ]
            
            if path.is_file():
                info.append(f"Is executable: {os.access(path, os.X_OK)}")
                info.append(f"Is readable: {os.access(path, os.R_OK)}")
                info.append(f"Is writable: {os.access(path, os.W_OK)}")
            
            return ToolResult(output="\n".join(info))
        except Exception as e:
            return ToolResult(error=f"Failed to get file info: {str(e)}")

    async def _change_permissions(self, path: Path, permissions: str) -> ToolResult:
        """Change file/directory permissions."""
        try:
            if not path.exists():
                return ToolResult(error=f"Path does not exist: {path}")
            
            # Convert octal string to integer
            perm_int = int(permissions, 8)
            path.chmod(perm_int)
            
            return ToolResult(output=f"Permissions changed to {permissions} for {path}")
        except ValueError:
            return ToolResult(error=f"Invalid permissions format: {permissions}. Use octal format like '755'")
        except Exception as e:
            return ToolResult(error=f"Failed to change permissions: {str(e)}")

    async def _find_files(self, path: Path, pattern: str, recursive: bool) -> ToolResult:
        """Find files matching a pattern."""
        try:
            if not path.exists():
                return ToolResult(error=f"Path does not exist: {path}")
            
            if not path.is_dir():
                return ToolResult(error=f"Path is not a directory: {path}")
            
            matches = []
            if recursive:
                matches = list(path.rglob(pattern))
            else:
                matches = list(path.glob(pattern))
            
            if not matches:
                return ToolResult(output=f"No files found matching pattern '{pattern}' in {path}")
            
            output = f"Files matching '{pattern}' in {path}:\n"
            for match in sorted(matches):
                rel_path = match.relative_to(path)
                file_type = "directory" if match.is_dir() else "file"
                output += f"{file_type:10} {rel_path}\n"
            
            return ToolResult(output=output)
        except Exception as e:
            return ToolResult(error=f"Failed to find files: {str(e)}")

    async def _get_file_size(self, path: Path) -> ToolResult:
        """Get the size of a file."""
        try:
            if not path.exists():
                return ToolResult(error=f"File does not exist: {path}")
            
            if not path.is_file():
                return ToolResult(error=f"Path is not a file: {path}")
            
            size = path.stat().st_size
            
            # Convert to human readable format
            for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    return ToolResult(output=f"File size: {size:.2f} {unit}")
                size /= 1024.0
            
            return ToolResult(output=f"File size: {size:.2f} PB")
        except Exception as e:
            return ToolResult(error=f"Failed to get file size: {str(e)}")

    async def _get_directory_size(self, path: Path) -> ToolResult:
        """Get the total size of a directory."""
        try:
            if not path.exists():
                return ToolResult(error=f"Directory does not exist: {path}")
            
            if not path.is_dir():
                return ToolResult(error=f"Path is not a directory: {path}")
            
            total_size = 0
            file_count = 0
            dir_count = 0
            
            for item in path.rglob("*"):
                if item.is_file():
                    total_size += item.stat().st_size
                    file_count += 1
                elif item.is_dir():
                    dir_count += 1
            
            # Convert to human readable format
            size = total_size
            for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    break
                size /= 1024.0
            
            output = [
                f"Directory: {path}",
                f"Total size: {size:.2f} {unit} ({total_size:,} bytes)",
                f"Files: {file_count:,}",
                f"Subdirectories: {dir_count:,}"
            ]
            
            return ToolResult(output="\n".join(output))
        except Exception as e:
            return ToolResult(error=f"Failed to get directory size: {str(e)}")
