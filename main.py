import logging
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from typing import Tuple

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


class DotEnvFileContentError(ValueError):
    pass


def verify_envvar_or_die(var_name: str) -> None:
    value = os.getenv(var_name)
    if value is None or len(value) == 0:
        logger.critical(f'{var_name} is not set')
        raise DotEnvFileContentError()


def load_dotenv_or_die() -> None:
    """Load .env file from disk"""
    load_dotenv()
    verify_envvar_or_die('usage-marker-start')
    verify_envvar_or_die('usage-marker-end')
    verify_envvar_or_die('readme-file')
    verify_envvar_or_die('patch-file')
    verify_envvar_or_die('patch-pattern')
    verify_envvar_or_die('header-content-file')
    verify_envvar_or_die('header-marker-start')
    verify_envvar_or_die('header-marker-end')
    verify_envvar_or_die('footer-content-file')
    verify_envvar_or_die('footer-marker-start')
    verify_envvar_or_die('footer-marker-end')


def get_env() -> Tuple:
    env_file = Path(".env")
    if env_file.is_file():
        load_dotenv_or_die()

    usage_m_start = os.environ["usage-marker-start"]
    usage_m_end = os.environ["usage-marker-end"]
    readme = os.environ["readme-file"]
    p_file = os.environ["patch-file"]
    p_pattern = os.environ["patch-pattern"]
    h_content_file = os.environ["header-content-file"]
    h_marker_start = os.environ["header-marker-start"]
    h_marker_end = os.environ["header-marker-end"]
    f_content_file = os.environ["footer-content-file"]
    f_marker_start = os.environ["footer-marker-start"]
    f_marker_end = os.environ["footer-marker-end"]
    return (
        usage_m_start,
        usage_m_end,
        readme,
        p_file,
        p_pattern,
        h_content_file,
        h_marker_start,
        h_marker_end,
        f_content_file,
        f_marker_start,
        f_marker_end
    )


def static_update(readme: str, m_start: str, m_end: str, content_file: str):
    copy_src_lines = True
    with open(content_file, 'rt') as c:
        content = c.read()
    with open(readme, 'rt') as s:
        source_file_content = s.readlines()
    with open(readme, 'wt') as t:
        for s_line in source_file_content:
            if copy_src_lines:
                t.writelines([s_line])
                if m_start in s_line:
                    copy_src_lines = False
                    t.write(f"{content}\n")
            else:
                if m_end in s_line:
                    t.writelines([s_line])
                    copy_src_lines = True
    logger.info("Static content is successfully updated")


def pickup_patch_doc(patching_file: str, patching_pattern: str):
    patch_file_content = []
    module_declaration_found = False
    with open(patching_file, 'rt') as p:
        for p_line in p:
            if not module_declaration_found:
                if p_line.startswith(patching_pattern):
                    module_declaration_found = True
                else:
                    continue
            patch_file_content.append(p_line)
    return patch_file_content


def usage_update(
    readme: str,
    usage_m_start: str,
    usage_m_end: str,
    patching_file: str,
    patching_pattern: str
):
    copy_src_lines = True
    with open(readme, 'rt') as s:
        source_file_content = s.readlines()
    with open(readme, 'wt') as t:
        for s_line in source_file_content:
            if copy_src_lines:
                t.writelines([s_line])
                if usage_m_start in s_line:
                    copy_src_lines = False
                    t.write("## Usage example\n")
                    t.write("```hcl\n")
                    t.writelines(
                        pickup_patch_doc(
                            patching_file,
                            patching_pattern
                        )
                    )
                    t.write("\n```\n")
            else:
                if usage_m_end in s_line:
                    t.writelines([s_line])
                    copy_src_lines = True
    logger.info("Script is successfully executed")


if __name__ == '__main__':
    (
        usage_marker_start,
        usage_marker_end,
        readme_file,
        patch_file,
        patch_pattern,
        header_content_file,
        header_marker_start,
        header_marker_end,
        footer_content_file,
        footer_marker_start,
        footer_marker_end
    ) = get_env()

    usage_update(
        readme=readme_file,
        usage_m_start=usage_marker_start,
        usage_m_end=usage_marker_end,
        patching_file=patch_file,
        patching_pattern=patch_pattern
    )
    # Header update
    static_update(
        readme=readme_file,
        m_start=header_marker_start,
        m_end=header_marker_end,
        content_file=header_content_file
    )
    # Footer update
    static_update(
        readme=readme_file,
        m_start=footer_marker_start,
        m_end=footer_marker_end,
        content_file=footer_content_file
    )
